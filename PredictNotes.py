import pathlib
import librosa
from tensorflow import keras
import numpy as np
from sklearn.preprocessing import LabelBinarizer
import glob
import re
import json


class PredictNotes:

  def __init__(self):
    self.FRAME_SIZE = int(2048 * 2)
    self.HOP_SIZE = int(self.FRAME_SIZE / 32)
    self.FRAMES_PER_IMAGE = 1
    self.TEST_VAL_SET_SIZE = 0.3
    self.EPOCHS = 10
    self.REQUIRED_DURATION_TO_BE_NOTE = 1/8

  def convert_audio_to_spectrogram(self, audio_sample):
    stft_audio = librosa.stft(
        audio_sample, n_fft=self.FRAME_SIZE, hop_length=self.HOP_SIZE)
    y_scale = np.abs(stft_audio) ** 2
    y_log_scale = librosa.power_to_db(y_scale)
    min_mag = np.min(y_log_scale)
    y_log_scale = y_log_scale - min_mag
    max_mag = np.max(y_log_scale)
    y_log_scale = y_log_scale / max_mag
    return y_log_scale

  def filter_notes(self, y_prediction, fps):
    y_prediction_filtered = []
    prev_elem = None
    curr_elem_length = 0
    required_frames_to_be_note = self.REQUIRED_DURATION_TO_BE_NOTE * fps
    for elemIdx in range(len(y_prediction)):
        if y_prediction[elemIdx] != prev_elem:
            if curr_elem_length >= required_frames_to_be_note:
                for _ in range(curr_elem_length):
                    y_prediction_filtered.append(prev_elem)
            else:
                for _ in range(curr_elem_length):
                    y_prediction_filtered.append(47)
            prev_elem = y_prediction[elemIdx]
            curr_elem_length = 1
            continue
        curr_elem_length += 1
        if elemIdx == len(y_prediction) - 1:
            if curr_elem_length >= required_frames_to_be_note:
                for _ in range(curr_elem_length):
                    y_prediction_filtered.append(prev_elem)
    return y_prediction_filtered

  def convert_notes_dict_to_seconds_from_frames(self, notes, fps):
    notes_conv = {}
    for noteIdx in range(len(notes)):
      notes_conv[len(notes_conv)] = [notes[noteIdx][0] /
                                        fps, notes[noteIdx][1] / fps, notes[noteIdx][2]]
    return notes_conv

  def main(self, audio_track, sample_rate):
    length_of_track_s = len(audio_track) / sample_rate
    model = keras.models.load_model('./models/notePredictModel.h5')
    y_log_scale = self.convert_audio_to_spectrogram(audio_track)
    frames_per_second = len(y_log_scale[0]) / length_of_track_s
    data_images = []
    for frame in range(len(y_log_scale[0]) - self.FRAMES_PER_IMAGE):
        data_images.append(
            y_log_scale[:, frame:frame + self.FRAMES_PER_IMAGE])
    data_images = np.array(data_images)
    data_images = np.asarray(data_images)
    prediction = model.predict(data_images)
    y_prediction = np.argmax(prediction, axis=1)
    y_prediction_filtered = self.filter_notes(
        y_prediction, frames_per_second)
    with open(r'./resources/notes_list.json') as json_file:
        data = json.load(json_file)
    filtered_list_of_notes = []
    for i in range(len(y_prediction_filtered)):
        filtered_list_of_notes.append(data[y_prediction_filtered[i]])
    notes_dict = {}
    current_start_duration_name = []
    for note_frame_idx in range(len(filtered_list_of_notes)):
        note_name = filtered_list_of_notes[note_frame_idx]
        if current_start_duration_name and note_frame_idx == len(filtered_list_of_notes) - 1:
            notes_dict[len(notes_dict)] = current_start_duration_name
        if not current_start_duration_name and note_name != 'na':
            current_start_duration_name = [note_frame_idx, 1, note_name]
            continue
        elif note_name == 'na':
            continue
        if note_name != current_start_duration_name[2]:
            notes_dict[len(notes_dict)] = current_start_duration_name
            current_start_duration_name = []
        else:
            current_start_duration_name[1] = current_start_duration_name[1] + 1
    notes_dict_s = self.convert_notes_dict_to_seconds_from_frames(
        notes_dict, frames_per_second)
    return notes_dict_s