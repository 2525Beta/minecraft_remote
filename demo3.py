from mcje.minecraft import Minecraft
import param_MCJE as param
import axis_flat

mc = Minecraft.create(port=param.PORT_MC)

axis_flat.reset_minecraft_world(mc, width=40)

mc.setBlocks(0, 63, 0,  30, 93, 30,  param.GOLD_BLOCK)
mc.setBlocks(-31, 63, -1,  1, 93, -31,  param.IRON_BLOCK)