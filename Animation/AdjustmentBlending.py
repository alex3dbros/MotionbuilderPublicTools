# This script is going to blend the adjustments over the places where you have more motion

if False: from pyfbsdk_gen_doc import *

from pyfbsdk import *
import Animation.EffectorList as EffectorList
reload(EffectorList)

effectors = EffectorList.CharacterEffectors
AnimBegin = FBSystem().CurrentTake.LocalTimeSpan.GetStart().GetFrame()
loop_count = FBSystem().CurrentTake.LocalTimeSpan.GetStop().GetFrame() - FBSystem().CurrentTake.LocalTimeSpan.GetStart().GetFrame()

System = FBSystem()

# This function is used to apply the keys on the curves
def create_animation(pNode, frame, value):
	if pNode.FCurve:
		xfcurve = pNode.FCurve
		xfcurve.KeyAdd(FBTime(0,0,0,frame), value)
	if pNode.Nodes:
		for lNode in pNode.Nodes:
			CreateAnimation( lNode )

# Function fo summing the keys from the base layer
def sum_keys(node):
	fcurve = node.FCurve
	sum_of_keys = 0
	if len(fcurve.Keys) > 20:
		for frame in range(0, len(fcurve.Keys)-1):
			dif_val = fcurve.Keys[frame+1].Value - fcurve.Keys[frame].Value
			sum_of_keys += abs(dif_val)
	else:
		for frame in range(len(fcurve.Keys)-1):
			dif_val = fcurve.Keys[frame+1].Value - fcurve.Keys[frame].Value
			sum_of_keys += abs(dif_val)
	return sum_of_keys

# Calculating the percentage
def base_keys_percentage(node, total):
	fcurve = node.FCurve
	percentage = []
	for frame in range(0, len(fcurve.Keys)-1):
		if total != 0:
			percent_value = (abs(fcurve.Keys[frame+1].Value) - abs(fcurve.Keys[frame].Value)) / total
		else:
			percent_value = 0
		percentage.append(abs(percent_value))

	return percentage

# Setting the layer
def set_active_layer(layer):

	if layer == 0:
		lCount = System.CurrentTake.GetLayerCount()
		System.CurrentTake.GetLayer(lCount-1).Name= "AdjustmentBlend"
		System.CurrentTake.GetLayerByName("AdjustmentBlend").SelectLayer(False, False)
		System.CurrentTake.SetCurrentLayer(layer)

	if layer > 0:
		# Setting the Adjustment layer as the active one
		System.CurrentTake.SetCurrentLayer(layer)
		System.CurrentTake.GetLayerByName("BaseAnimation").SelectLayer(False, False)
		System.CurrentTake.GetLayerByName("AdjustmentBlend").SelectLayer(True, False)

# Applying the blend for each node that's been feed in
def apply_blending(anim_objects):
	if anim_objects.Nodes:
		for node in anim_objects.Nodes:
			# setting the base layer as the active one
			set_active_layer(0)

			sum_of_keys = sum_keys(node)
			keys_percentage = base_keys_percentage(node, sum_of_keys)

			set_active_layer(1)
			# calculating the sum of adjustment layer keys
			adjustment_sum = sum_keys(node)

			if adjustment_sum != 0:
				for frame in range(0, len(keys_percentage)-1):
					if frame == 0:
						if node.FCurve.Keys[frame].Value > 0:
							create_animation(node, frame, (node.FCurve.Keys[frame].Value + (keys_percentage[frame]  * adjustment_sum)))

						if node.FCurve.Keys[frame].Value < 0:
							create_animation(node, frame, (node.FCurve.Keys[frame].Value - (keys_percentage[frame]  * adjustment_sum)))
					else:
						if node.FCurve.Keys[frame].Value > 0:
							create_animation(node, frame, (node.FCurve.Keys[frame-1].Value + (keys_percentage[frame]  * adjustment_sum)))

						if node.FCurve.Keys[frame].Value < 0:
							create_animation(node, frame, (node.FCurve.Keys[frame-1].Value - (keys_percentage[frame]  * adjustment_sum)))

# Calling the apply blending function
def adjustment_blending(object_to_blend):
	# apply blending on Translation nodes
	apply_blending(object_to_blend.Translation.GetAnimationNode())

	# apply blending on Rotation nodes
	# apply_blending(object_to_blend.Rotation.GetAnimationNode())




# List of all IK effectors
# custom_list = (EffectorList.Hips, EffectorList.LAnkle, EffectorList.RAnkle, EffectorList.LKnee, EffectorList.RKnee, EffectorList.LFoot, EffectorList.RFoot, EffectorList.LHip, EffectorList.RHip)

# small trial list
custom_list = (EffectorList.Hips, EffectorList.LAnkle, EffectorList.RAnkle)

def adjust():

	for effector in custom_list:
		adjustment_blending(effector)

	print "Adjusted"

adjust()