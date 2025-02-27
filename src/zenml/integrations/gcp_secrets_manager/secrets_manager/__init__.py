#  Copyright (c) ZenML GmbH 2022. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at:
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#  or implied. See the License for the specific language governing
#  permissions and limitations under the License.
"""
## Secrets Manager
The GCP Secrets Manager allows your pipeline to directly access the GCP
secrets manager and use the secrets within during runtime.
"""
from zenml.integrations.gcp_secrets_manager.secrets_manager.gcp_secrets_manager import (
    GCPSecretsManager,
)

__all__ = ["GCPSecretsManager"]
