import fire
import json
import os
import tensorflow as tf
import pickle
import pandas
import numpy
from sklearn.preprocessing import StandardScaler

COLUMN_NAMES = ['sepal_len', 'sepal_width', 'petal_len', 'petal_width', 'label']

def configure(outpath):
    scaler = StandardScaler(with_mean=False, with_std=False)
    with open(outpath, "wb") as f:
        pickle.dump(scaler, f)
        
        
def build_scaler(config_path):
    with open(config_path, "rb") as f:
        scaler = pickle.load(f)
    return scaler


def define_model():
    model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(4,)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')])
    model.compile(optimizer='adam', loss=tf.keras.losses.CategoricalCrossentropy(), metrics=['accuracy'])
    return model
    

def train_model(dataset_path, config_path, out_path, epochs=2):
    dataset = dataset_path
    config = config_path
    scaler = build_scaler(config_path)
    
    df = pandas.read_csv(dataset_path, header=None, names=COLUMN_NAMES, sep=',')
    df['label'] = pandas.Categorical(df['label'])
    df['label'] = df.label.cat.codes
    label = df.pop("label").values.astype(numpy.float)
    one_hot = tf.keras.backend.one_hot(tf.convert_to_tensor(label, dtype=tf.int32), 3)
    training_data = scaler.fit_transform(df)
    dataset = tf.data.Dataset.from_tensor_slices((training_data, one_hot))
    feed = dataset.shuffle(len(training_data)).batch(10)
    model = define_model()
    model.fit(feed, epochs=epochs)
    model.save(out_path)
        
        
def export(model_path, out_path):
    model_path = model_path
    model = tf.keras.models.load_model(model_path)
    model.save(out_path) 
    
        
if __name__ == '__main__':
  fire.Fire()