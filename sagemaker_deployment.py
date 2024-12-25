import sagemaker
from sagemaker import get_execution_role
from sagemaker.pytorch import PyTorchModel

def deploy_model():
    role = get_execution_role()
    
    model = PyTorchModel(
        model_data="s3://path/to/your/model.tar.gz",
        role=role,
        entry_point="inference.py",
        framework_version="1.5.0",
    )
    
    predictor = model.deploy(
        instance_type="ml.m5.large", 
        initial_instance_count=1
    )

if __name__ == "__main__":
    deploy_model()
