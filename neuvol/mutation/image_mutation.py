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
import numpy as np

from .base_mutation import MutatorBase
from .mutation_modules import perform_mutation


class MutatorImage(MutatorBase):
    """
    Mutator class for visual data
    """

    @staticmethod
    def mutate(individ):
        """
        Mutate individ
        """
        super().mutate()

        mutation_type = np.random.choice([
            'architecture_part',
            'architecture_parameters',
            'training_all',
            'training_part',
            'architecture_add',
            'architecture_remove'
        ])

        individ = perform_mutation(individ, mutation_type)

        return individ
