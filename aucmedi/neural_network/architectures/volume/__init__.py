#==============================================================================#
#  Author:       Dominik Müller                                                #
#  Copyright:    2022 IT-Infrastructure for Translational Medical Research,    #
#                University of Augsburg                                        #
#                                                                              #
#  This program is free software: you can redistribute it and/or modify        #
#  it under the terms of the GNU General Public License as published by        #
#  the Free Software Foundation, either version 3 of the License, or           #
#  (at your option) any later version.                                         #
#                                                                              #
#  This program is distributed in the hope that it will be useful,             #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of              #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
#  GNU General Public License for more details.                                #
#                                                                              #
#  You should have received a copy of the GNU General Public License           #
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.       #
#==============================================================================#
# Abstract Base Class for Architectures
from aucmedi.neural_network.architectures.arch_base import Architecture_Base

#-----------------------------------------------------#
#                    Architectures                    #
#-----------------------------------------------------#
# Vanilla Classifier
from aucmedi.neural_network.architectures.volume.vanilla import Architecture_Vanilla
# DenseNet
from aucmedi.neural_network.architectures.volume.densenet121 import Architecture_DenseNet121
from aucmedi.neural_network.architectures.volume.densenet169 import Architecture_DenseNet169
from aucmedi.neural_network.architectures.volume.densenet201 import Architecture_DenseNet201

#-----------------------------------------------------#
#       Access Functions to Architecture Classes      #
#-----------------------------------------------------#
# Architecture Dictionary
architecture_dict = {
    "Vanilla": Architecture_Vanilla,
    "DenseNet121": Architecture_DenseNet121,
    "DenseNet169": Architecture_DenseNet169,
    "DenseNet201": Architecture_DenseNet201,
}
# List of implemented architectures
architectures = list(architecture_dict.keys())

#-----------------------------------------------------#
#       Meta Information of Architecture Classes      #
#-----------------------------------------------------#
# Utilized standardize mode of architectures required for Transfer Learning
supported_standardize_mode = {
    "Vanilla": "z-score",
    "DenseNet121": "torch",
    "DenseNet169": "torch",
    "DenseNet201": "torch",
}