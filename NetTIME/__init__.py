"""
NetTIME: A multitask learning model for prediction base-pair resolution
in vivo TF binding predictions using embeddings.
"""
from .trainer import TrainWorkflow
from .evaluator import EvaluateWorkflow
from .predictor import PredictWorkflow

from .crf_trainer import CRFTrainWorkflow
from .crf_evaluator import CRFEvaluateWorkflow
from .crf_predictor import CRFPredictWorkflow

__version__ = "0.1.0"
