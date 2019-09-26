#   Copyright 2019 - qthought
#
#   Licensed under the MIT License;
#   you may not use this file except in compliance with the License.
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from ._version import __version__
from qthought.logicalReasoning import consistency
from qthought.interpretations import collapse_theory, copenhagen_theory
from qthought.utils import arithmeticgates, general, subspace

#from qthought.int
#from . import agents
#from . import quantumsystem
#from . import C
#from . import inference_procedures

from .quantumsystem import QuantumSystem
from .protocol import ProtocolStep, Protocol