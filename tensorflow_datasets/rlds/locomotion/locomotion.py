# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
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

"""Locomotion dataset."""

import tensorflow as tf
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.rlds import rlds_base

_DESCRIPTION = """
The datasets were created with a SAC agent trained on the environment reward of
MuJoCo locomotion tasks. These datasets are used in
[What Matters for Adversarial Imitation Learning? Orsini et al. 2021](https://arxiv.org/pdf/2106.00672.pdf).
"""

_CITATION = """
  @article{orsini2021matters,
    title={What Matters for Adversarial Imitation Learning?},
    author={Orsini, Manu and Raichuk, Anton and Hussenot, L{\'e}onard and Vincent, Damien and Dadashi, Robert and Girgin, Sertan and Geist, Matthieu and Bachem, Olivier and Pietquin, Olivier and Andrychowicz, Marcin},
    journal={International Conference in Machine Learning},
    year={2021}
  }
"""

_HOMEPAGE = 'https://github.com/google-research/rlds'


class Locomotion(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for locomotion dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  _DATA_PATHS = {
      'ant_sac_1M_single_policy_stochastic':
          'https://storage.googleapis.com/rlds_external_data_release/ant_sac_1M_single_policy_stochastic.tar.gz',
      'walker2d_sac_1M_single_policy_stochastic':
          'https://storage.googleapis.com/rlds_external_data_release/walker2d_sac_1M_single_policy_stochastic.tar.gz',
      'humanoid_sac_15M_single_policy_stochastic':
          'https://storage.googleapis.com/rlds_external_data_release/humanoid_sac_15M_single_policy_stochastic.tar.gz',
      'hopper_sac_1M_single_policy_stochastic':
          'https://storage.googleapis.com/rlds_external_data_release/hopper_sac_1M_single_policy_stochastic.tar.gz',
      'halfcheetah_sac_1M_single_policy_stochastic':
          'https://storage.googleapis.com/rlds_external_data_release/halfcheetah_sac_1M_single_policy_stochastic.tar.gz',
  }

  BUILDER_CONFIGS = [
      rlds_base.DatasetConfig(
          name='ant_sac_1M_single_policy_stochastic',
          observation_info=tfds.features.Tensor(shape=(111,), dtype=tf.float32),
          action_info=tfds.features.Tensor(shape=(8,), dtype=tf.float32),
          reward_info=tf.float32,
          discount_info=tf.float32,
          citation=_CITATION,
          homepage=_HOMEPAGE,
          overall_description=_DESCRIPTION,
          description='Dataset generated by a SAC agent trained for 1M steps for Ant.',
          supervised_keys=None,  # pytype: disable=wrong-arg-types  # gen-stub-imports
      ),
      rlds_base.DatasetConfig(
          name='hopper_sac_1M_single_policy_stochastic',
          observation_info=tfds.features.Tensor(shape=(11,), dtype=tf.float32),
          action_info=tfds.features.Tensor(shape=(3,), dtype=tf.float32),
          reward_info=tf.float32,
          discount_info=tf.float32,
          citation=_CITATION,
          homepage=_HOMEPAGE,
          overall_description=_DESCRIPTION,
          description='Dataset generated by a SAC agent trained for 1M steps for Hopper.',
          supervised_keys=None,  # pytype: disable=wrong-arg-types  # gen-stub-imports
      ),
      rlds_base.DatasetConfig(
          name='halfcheetah_sac_1M_single_policy_stochastic',
          observation_info=tfds.features.Tensor(shape=(17,), dtype=tf.float32),
          action_info=tfds.features.Tensor(shape=(6,), dtype=tf.float32),
          reward_info=tf.float32,
          discount_info=tf.float32,
          citation=_CITATION,
          homepage=_HOMEPAGE,
          overall_description=_DESCRIPTION,
          description='Dataset generated by a SAC agent trained for 1M steps for HalfCheetah.',
          supervised_keys=None,  # pytype: disable=wrong-arg-types  # gen-stub-imports
      ),
      rlds_base.DatasetConfig(
          name='walker2d_sac_1M_single_policy_stochastic',
          observation_info=tfds.features.Tensor(shape=(17,), dtype=tf.float32),
          action_info=tfds.features.Tensor(shape=(6,), dtype=tf.float32),
          reward_info=tf.float32,
          discount_info=tf.float32,
          citation=_CITATION,
          homepage=_HOMEPAGE,
          overall_description=_DESCRIPTION,
          description='Dataset generated by a SAC agent trained for 1M steps for Walker2d.',
          supervised_keys=None,  # pytype: disable=wrong-arg-types  # gen-stub-imports
      ),
      rlds_base.DatasetConfig(
          name='humanoid_sac_15M_single_policy_stochastic',
          observation_info=tfds.features.Tensor(shape=(376,), dtype=tf.float32),
          action_info=tfds.features.Tensor(shape=(17,), dtype=tf.float32),
          reward_info=tf.float32,
          discount_info=tf.float32,
          citation=_CITATION,
          homepage=_HOMEPAGE,
          overall_description=_DESCRIPTION,
          description='Dataset generated by a SAC agent trained for 15M steps for Humanoid.',
          supervised_keys=None,  # pytype: disable=wrong-arg-types  # gen-stub-imports
      ),
  ]


  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return rlds_base.build_info(self.builder_config, self)

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    path = dl_manager.download_and_extract({
        'file_path': self._DATA_PATHS[self.builder_config.name],
    })
    return {
        'train': self._generate_examples(path),
    }

  def _generate_examples(self, path):
    """Yields examples."""
    file_path = path['file_path']
    return rlds_base.generate_examples(file_path)