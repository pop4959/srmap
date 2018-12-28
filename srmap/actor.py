from enum import Enum

class ActorType(Enum):
	# These are all of the currently in-use actors in the game. Many of them will crash the game when used in a map.
	PLAYER = "Player"
	SPAWN_POINT = "SpawnPoint"
	TRIGGER_SAW = "TriggerSaw"
	GRAPHIC = "Deco"
	GRAPHIC_LIGHT = "DecoLight"
	GRAHPIC_GLOW = "DecoGlow"
	TEXT = "TextDeco"
	AIVOLUME = "AIVolume"
	BOOST_SECTION = "BoostSection"
	BLACK_CRATE = "FallTile"
	SWITCH = "SwitchBlock"
	FALLING_BLOCK = "FallingBlock"
	FINISH_TRIGGER = "FinishTrigger"
	SPIKE = "LethalObstacle"
	CRATE = "Obstacle";
	PLAYER_START = "PlayerStart"
	DOOR = "Door"
	TRIGGER = "Trigger"
	SWITCH = "Switch"
	SUPER_BOOST_SPRITE = "SuperBoostSprite"
	TREE = "Tree"
	DOVE = "Dove"
	EDITABLE_SOUND_EMITTER = "EditableSoundEmitter"
	EDITABLE_SOUND_EMITTER_VOLUME = "EditableSoundEmitterVolume"
	SMOKE_EMITTER = "SmokeEmitter"
	ITEM_PICKUP = "Pickup"
	CHECKPOINT = "Checkpoint"
	SIGN = "Sign"
	ROCKET_LAUNCHER = "RocketLauncher"
	SAW_STATIC = "SawStatic"
	SAW_UP_DOWN = "SawUpDown"
	SAW_CIRCLE = "SawCircle"
	MOVING_SAWS = "MovingSaws"
	BUBBLES = "Bubbles"
	BOOKCASE = "Bookcase"
	METRO_TUNNEL = "MetroTunnel"
	LEAVES = "Leaves"
	LASER = "Laser"
	PUMP = "Pump"
	SPARK = "Spark"
	GEAR = "Gear"
	BOSS = "Boss"
	SUPER_BOOST_TRIGGER_U = "SuperBoostTriggerU"
	SUPER_BOOST_TRIGGER_UR = "SuperBoostTriggerUR"
	SUPER_BOOST_TRIGGER_R = "SuperBoostTriggerR"
	SUPER_BOOST_TRIGGER_DR = "SuperBoostTriggerDR"
	SUPER_BOOST_TRIGGER_D = "SuperBoostTriggerD"
	SUPER_BOOST_TRIGGER_DL = "SuperBoostTriggerDL"
	SUPER_BOOST_TRIGGER_L = "SuperBoostTriggerL"
	SUPER_BOOST_TRIGGER_UL = "SuperBoostTriggerUL"
	SUPER_BOOST_TRIGGER_END = "SuperBoostTriggerEnd"
	SUPER_BOOST_VOLUME = "SuperBoostVolume"

class Actor:
    def __init__(self, position=(0, 0), size=(0, 0), type='', properties=None):
        self.position = position
        self.size = size
        self.type = type
        self.properties = [] if properties is None else properties
