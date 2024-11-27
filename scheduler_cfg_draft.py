import os

datasets =["dataset1", "dataset2"]
models = ["model1", "model2"]

# создает набор упорядоченных пар (dataset - model)
# [("dataset1", "model1"), dataset - model
# ("dataset1", "model2"),
# ("dataset2", "model1"),
# ("dataset2", "model2")]

class BenchmarkScheduler():
    """Планировщик бенчмарка
    """    
    def __init__(self, models, datasets, dvc_params_yaml_path):
        self.models = models
        self.datasets = datasets
        self.dvc_params_yaml_path = dvc_params_yaml_path

    def update_params_yaml(self, dataset, model):
        """Обновить параметры dataset и model в self.self.dvc_params_yaml_path
        yaml-файле осуществляющим бенчмарк 1 модели на 1 датасете

        Parameters
        ----------
        dataset : _type_
            _description_
        model : _type_
            _description_
        """        
        pass
    
    def run_bencmarks(self):
        """Запускает бенчмарк всех моделей на всех датасетах
        """        
        for dataset in datasets:
            for model in models:
                # заходит в параметры params.yaml
                # устанавливает
                # dataset -> dataset1
                # model -> model1
                self.update_params_yaml(dataset, model)
                
                # DVC Не будет выполнять уже вычисленные им
                # бенчмарки (dataset - model)
                # оптимизация
                os.system("dvc repro")

