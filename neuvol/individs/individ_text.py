# Copyright 2018 Timur Sokhin.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from .individ_base import IndividBase
from ..layer import Layer
from .structure import StructureText


class IndividText(IndividBase):
    """
    Invidiv class for text data types
    """

    def __init__(self, stage, options, finisher, distribution, task_type='classification', parents=None, freeze=None):
        super().__init__(stage=stage, options=options, finisher=finisher, distribution=distribution, task_type=task_type, parents=parents, freeze=freeze)
        self._data_processing_type = 'text'

    def _random_init_architecture(self):
        """
        At first, we set probabilities pool and the we change
        this uniform distribution according to previous layer
        """
        input_layer = Layer('input', self._distribution, self.options)
        embed = Layer('embedding', self._distribution, self.options)

        architecture = StructureText(input_layer, embed, self._finisher)

        return architecture

    def _random_init_data_processing(self):
        """
        Init structure of the individ
        """
        data_tmp = {}
        data_tmp['vocabular'] = self._architecture.layers_index_reverse[1].config['vocabular']
        data_tmp['sentences_length'] = self.options.get('shape', [10])[0]
        data_tmp['classes'] = self.options.get('classes', 2)

        return data_tmp

    # @staticmethod
    # def load(self, serial):
    #     """
    #     Load method. Returns individ
    #     """
    #     individ = IndividText(serial['stage'])

    #     individ._stage = serial['stage']
    #     individ._data_processing_type = serial['data_processing_type']
    #     individ._task_type = serial['task_type']
    #     individ._freeze = serial['freeze']
    #     if serial['parents'] is not None:
    #         individ._parents = [IndividBase(serial['stage'] - 1), IndividBase(serial['stage'] - 1)]
    #         individ._parents = [parent.load(serial['parents'][i]) for i, parent in enumerate(self._parents)]
    #     individ.options = serial['options']
    #     individ._history = serial['history']
    #     individ._name = serial['name']

    #     individ._architecture = [Block('input', layers_number=1, **self.options) \
    #         for i, _ in enumerate(serial['architecture'])]
    #     individ._architecture = [block.load(serial['architecture'][i]) for i, block in enumerate(self._architecture)]

    #     individ._data_processing = serial['data_processing']
    #     individ._training_parameters = serial['training_parameters']
    #     individ._layers_number = serial['layers_number']
    #     individ._result = serial['result']
    #     individ.shape_structure = serial['shape_structure']

    #     return individ
