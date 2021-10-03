#  Copyright (c) ZenML GmbH 2021. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at:
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#  or implied. See the License for the specific language governing
#  permissions and limitations under the License.

import os

import pandas as pd

from zenml.materializers.base_materializer import BaseMaterializer

DEFAULT_FILENAME = "data.csv"


class PandasMaterializer(BaseMaterializer):
    """ """

    @staticmethod
    def read(input_artifact, filename=None):
        """ """
        filepath = os.path.join(
            input_artifact.uri,
            filename if filename is not None else DEFAULT_FILENAME
        )

        return pd.read_csv(filepath)

    @staticmethod
    def write(output_artifact, df, filename=None):
        """ """
        filepath = os.path.join(
            output_artifact.uri,
            filename if filename is not None else DEFAULT_FILENAME
        )

        df.to_csv(filepath)
