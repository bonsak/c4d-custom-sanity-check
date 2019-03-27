import c4d
from c4d import documents
from c4d import gui

def RunSanityCheck( dialog ):
	# Most of this code is copied from the main submitter.
    scene = documents.GetActiveDocument()
    frameRate = scene.GetFps()

    startFrame = 0
    endFrame = 0
    stepFrame = 0
    midFrame = 0
    
    renderData = scene.GetActiveRenderData().GetData()
    frameMode = renderData.GetLong( c4d.RDATA_FRAMESEQUENCE )

    if frameMode == c4d.RDATA_FRAMESEQUENCE_MANUAL:
        startFrame = renderData.GetTime( c4d.RDATA_FRAMEFROM ).GetFrame( frameRate )
        endFrame = renderData.GetTime( c4d.RDATA_FRAMETO ).GetFrame( frameRate )
        stepFrame = renderData.GetLong( c4d.RDATA_FRAMESTEP )
    elif frameMode == c4d.RDATA_FRAMESEQUENCE_CURRENTFRAME:
        startFrame = scene.GetTime().GetFrame( frameRate )
        endFrame = startFrame
        stepFrame = 1
    elif frameMode == c4d.RDATA_FRAMESEQUENCE_ALLFRAMES:
        startFrame = scene.GetMinTime().GetFrame( frameRate )
        endFrame = scene.GetMaxTime().GetFrame( frameRate )
        stepFrame = renderData.GetLong( c4d.RDATA_FRAMESTEP )
    elif frameMode == c4d.RDATA_FRAMESEQUENCE_PREVIEWRANGE:
        startFrame = scene.GetLoopMinTime().GetFrame( frameRate )
        endFrame = scene.GetLoopMaxTime().GetFrame( frameRate )
        stepFrame = renderData.GetLong( c4d.RDATA_FRAMESTEP )
    
    frameList = str(startFrame)
    if startFrame != endFrame:
    	# Find a frame in the middle of the range
    	midFrame = int(endFrame * 0.5)
        frameList = frameList + "-" + str(endFrame)
        # Build a custom range with first, last, middleframe and then all the frames
        frameList = '{0},{1},{2},{0}-{1}'.format(startFrame, endFrame, midFrame )
    if stepFrame > 1:
        frameList = frameList + "x" + str(stepFrame)

    # print 'Start {}, End {}, Step {}'.format(startFrame, endFrame, stepFrame)
    # print frameList

    dialog.SetString( dialog.dialogIDs[ "FramesBoxID" ], frameList )

    return True