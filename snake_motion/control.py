"""
Responsável por
    - Gerenciar o jogo
    - Utilizar módulos de entrada e saída

Corresponde à lógica principal do projeto.
"""
from snake_motion.game.models import Game
from snake_motion.input_manager.giroscope_manager import Giroscope
from snake_motion.output_manager.gpio_manager import GPIO