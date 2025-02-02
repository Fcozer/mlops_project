import dagshub
import mlflow

mlflow.set_tracking_uri("https://dagshub.com/Fcozer/mlops_project.mlflow")

dagshub.init(repo_owner='Fcozer', repo_name='mlops_project', mlflow=True)

with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)