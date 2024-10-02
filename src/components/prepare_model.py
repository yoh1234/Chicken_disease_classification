from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass
from pathlib import Path
import os
import sys

import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications.vgg16 import VGG16


@dataclass(frozen=True)
class BaseModelConfig:
    root_dir: Path = os.path.join("artifacts", "cnn_model")
    base_model_path: Path = os.path.join("artifacts", "cnn_model", "base_model.h5")
    updated_model_path: Path = os.path.join("artifacts", "cnn_model", "transfered_cnn_model.h5")
    # Hyperparameters
    image_size: list = (224, 224, 3)
    learning_rate: float = 0.01
    include_top: bool = False
    weights: str = "imagenet"
    classes: int = "5"

class PrepareBaseCnnModel:
    def __init__(self):
        self.basemodel_config = BaseModelConfig()
    
    def save_model(self, path: Path, model: tf.keras.Model):
        model.save(path)
    
    def prepare_full_cnn_model(self, freeze_all: bool):

        self.basemodel = VGG16(
            input_shape = self.basemodel_config.image_size,
            weights=self.basemodel_config.weights,
            include_top=self.basemodel_config.include_top
        )
        if freeze_all:
            self.basemodel.trainable = False

        flatten_layer = layers.Flatten()
        dense_layer_1 = layers.Dense(50, activation = 'relu')
        dense_layer_2 = layers.Dense(20, activation = 'relu')
        prediction_layer = layers.Dense(5, activation = 'softmax')

        full_model = models.Sequential([
            self.basemodel,
            flatten_layer,
            dense_layer_1,
            dense_layer_2,
            prediction_layer
        ])
        self.save_model(path=self.basemodel_config.updated_model_path, model=full_model)


