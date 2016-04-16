from pyfbsdk import *
from pyfbsdk_additions import *

# defining Control Rig
if FBApplication().CurrentCharacter:
    character = FBApplication().CurrentCharacter
    Hips = character.GetEffectorModel(FBEffectorId.kFBHipsEffectorId)
    LAnkle = character.GetEffectorModel(FBEffectorId.kFBLeftAnkleEffectorId)
    RAnkle = character.GetEffectorModel(FBEffectorId.kFBRightAnkleEffectorId)
    LWrist = character.GetEffectorModel(FBEffectorId.kFBLeftWristEffectorId)
    RWrist = character.GetEffectorModel(FBEffectorId.kFBRightWristEffectorId)
    LKnee = character.GetEffectorModel(FBEffectorId.kFBLeftKneeEffectorId)
    RKnee = character.GetEffectorModel(FBEffectorId.kFBRightKneeEffectorId)
    LElbow = character.GetEffectorModel(FBEffectorId.kFBLeftElbowEffectorId)
    RElbow = character.GetEffectorModel(FBEffectorId.kFBRightElbowEffectorId)
    ChestOrigin = character.GetEffectorModel(FBEffectorId.kFBChestOriginEffectorId)
    ChestEnd = character.GetEffectorModel(FBEffectorId.kFBChestEndEffectorId)
    LFoot = character.GetEffectorModel(FBEffectorId.kFBLeftFootEffectorId)
    RFoot = character.GetEffectorModel(FBEffectorId.kFBRightFootEffectorId)
    LShoulder = character.GetEffectorModel(FBEffectorId.kFBLeftShoulderEffectorId)
    RShoulder = character.GetEffectorModel(FBEffectorId.kFBRightShoulderEffectorId)
    Head = character.GetEffectorModel(FBEffectorId.kFBHeadEffectorId)
    LHip = character.GetEffectorModel(FBEffectorId.kFBLeftHipEffectorId)
    RHip = character.GetEffectorModel(FBEffectorId.kFBRightHipEffectorId)
    # LHand = character.GetEffectorModel(FBEffectorId.kFBLeftHandEffectorId)
    # RHand = character.GetEffectorModel(FBEffectorId.kFBRightHandEffectorId)
    LHandThumb = character.GetEffectorModel(FBEffectorId.kFBLeftHandThumbEffectorId)
    LHandIndex = character.GetEffectorModel(FBEffectorId.kFBLeftHandIndexEffectorId)
    LHandMiddle = character.GetEffectorModel(FBEffectorId.kFBLeftHandMiddleEffectorId)
    LHandRing = character.GetEffectorModel(FBEffectorId.kFBLeftHandRingEffectorId)
    LHandPinky = character.GetEffectorModel(FBEffectorId.kFBLeftHandPinkyEffectorId)
    RHandThumb = character.GetEffectorModel(FBEffectorId.kFBRightHandThumbEffectorId)
    RHandIndex = character.GetEffectorModel(FBEffectorId.kFBRightHandIndexEffectorId)
    RHandMiddle = character.GetEffectorModel(FBEffectorId.kFBRightHandMiddleEffectorId)
    RHandRing = character.GetEffectorModel(FBEffectorId.kFBRightHandRingEffectorId)
    RHandPinky = character.GetEffectorModel(FBEffectorId.kFBLeftHandPinkyEffectorId)

    CharacterEffectors = [Hips, LAnkle, RAnkle, LWrist, RWrist, LKnee, RKnee, LElbow, RElbow,
                          ChestOrigin, ChestEnd, LFoot, RFoot, LShoulder, RShoulder, Head, LHip,
                          RHip, LHandThumb, LHandIndex, LHandMiddle, LHandRing,
                          LHandPinky, RHandThumb, RHandIndex, RHandMiddle, RHandRing, RHandPinky]
