import kfp
from kfp import dsl
import kfp.components as comp


composant_Rscript = comp.load_component_from_file("composant.yml")

@dsl.pipeline(
    name='my-first-pipeline',
    description='A R pipeline.'
)
def test_pipeline():
    data_csv = composant_Rscript().output

if __name__ == '__main__':
    kfp.compiler.Compiler().compile(test_pipeline, __file__ + '.yaml')