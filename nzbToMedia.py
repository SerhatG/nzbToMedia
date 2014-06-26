#!/usr/bin/env python2
#
##############################################################################
### NZBGET POST-PROCESSING SCRIPT                                          ###

# Post-Process to CouchPotato, SickBeard, NzbDrone, Mylar, Gamez, HeadPhones.
#
# This script sends the download to your automated media management servers.
#
# NOTE: This script requires Python to be installed on your system.

##############################################################################
### OPTIONS                                                                ###

## General

# Auto Update nzbToMedia (0, 1).
#
# Set to 1 if you want nzbToMedia to automatically check for and update to the latest version
#auto_update=0

# Check Media for corruption (0, 1).
#
# Enable/Disable media file checking using ffprobe.
#check_media=1

# Safe Mode protection of DestDir (0, 1).
#
# Enable/Disable a safety check to ensure we don't process all downloads in the default_downloadDirectory by mistake.
#safe_mode=1

## CouchPotato

# CouchPotato script category.
#
# category that gets called for post-processing with CouchPotatoServer.
#cpsCategory=movie

# CouchPotato api key.
#cpsapikey=

# CouchPotato host.
#cpshost=localhost

# CouchPotato port.
#cpsport=5050

# CouchPotato uses ssl (0, 1).
#
# Set to 1 if using ssl, else set to 0.
#cpsssl=0

# CouchPotato URL_Base
#
# set this if using a reverse proxy.
#cpsweb_root=

# CouchPotato Postprocess Method (renamer, manage).
#
# use "renamer" for CPS renamer (default) or "manage" to call a manage update.
#cpsmethod=renamer

# CouchPotato Delete Failed Downloads (0, 1).
#
# set to 1 to delete failed, or 0 to leave files in place.
#cpsdelete_failed=0

# CouchPotato wait_for
#
# Set the number of minutes to wait after calling the renamer, to check the movie has changed status.
#cpswait_for=2

# Couchpotato and NZBGet are a different system (0, 1).
#
# Enable to replace local path with the path as per the mountPoints below.
#cpsremote_path=0

## SickBeard

# SickBeard script category.
#
# category that gets called for post-processing with SickBeard.
#sbCategory=tv

# SickBeard host.
#sbhost=localhost

# SickBeard port.
#sbport=8081

# SickBeard username.
#sbusername=

# SickBeard password.
#sbpassword=

# SickBeard uses ssl (0, 1).
#
# Set to 1 if using ssl, else set to 0.
#sbssl=0

# SickBeard web_root
#
# set this if using a reverse proxy.
#sbweb_root=

# SickBeard watch directory.
#
# set this if SickBeard and nzbGet are on different systems.
#sbwatch_dir=

# SickBeard fork.
#
# set to default or auto to auto-detect the custom fork type.
#sbfork=auto

# SickBeard Delete Failed Downloads (0, 1).
#
# set to 1 to delete failed, or 0 to leave files in place.
#sbdelete_failed=0

# SickBeard process method.
#
# set this to move, copy, hardlin, symlink as appropriate if you want to over-ride SB defaults. Leave blank to use SB default.
#sbprocess_method=

# SickBeard and NZBGet are a different system (0, 1).
#
# Enable to replace local path with the path as per the mountPoints below.
#sbremote_path=0

## NzbDrone

# NzbDrone script category.
#
# category that gets called for post-processing with NzbDrone.
#ndCategory=tv2

# NzbDrone host.
#ndhost=localhost

# NzbDrone port.
#ndport=8989

# NzbDrone API key.
#ndapikey=

# NzbDrone uses SSL (0, 1).
#
# Set to 1 if using SSL, else set to 0.
#ndssl=0

# NzbDrone web root.
#
# set this if using a reverse proxy.
#ndweb_root=

# NzbDrone wait_for
#
# Set the number of minutes to wait after calling the renamer, to check the episode has changed status.
#ndwait_for=2

# NzbDrone Delete Failed Downloads (0, 1).
#
# set to 1 to delete failed, or 0 to leave files in place.
#nddelete_failed=0

# NzbDrone and NZBGet are a different system (0, 1).
#
# Enable to replace local path with the path as per the mountPoints below.
#ndremote_path=0

## HeadPhones

# HeadPhones script category.
#
# category that gets called for post-processing with HeadHones.
#hpCategory=music

# HeadPhones api key.
#hpapikey=

# HeadPhones host.
#hphost=localhost

# HeadPhones port.
#hpport=8181

# HeadPhones uses ssl (0, 1).
#
# Set to 1 if using ssl, else set to 0.
#hpssl=0

# HeadPhones web_root
#
# set this if using a reverse proxy.
#hpweb_root=

# HeadPhones and NZBGet are a different system (0, 1).
#
# Enable to replace local path with the path as per the mountPoints below.
#hpremote_path=0

## Mylar

# Mylar script category.
#
# category that gets called for post-processing with Mylar.
#myCategory=comics

# Mylar host.
#myhost=localhost

# Mylar port.
#myport=8090

# Mylar username.
#myusername=

# Mylar password.
#mypassword=

# Mylar uses ssl (0, 1).
#
# Set to 1 if using ssl, else set to 0.
#myssl=0

# Mylar web_root
#
# set this if using a reverse proxy.
#myweb_root=

# Mylar wait_for
#
# Set the number of minutes to wait after calling the force process, to check the issue has changed status.
#myswait_for=1

# Mylar and NZBGet are a different system (0, 1).
#
# Enable to replace local path with the path as per the mountPoints below.
#myremote_path=0

## Gamez

# Gamez script category.
#
# category that gets called for post-processing with Gamez.
#gzCategory=games

# Gamez api key.
#gzapikey=

# Gamez host.
#gzhost=localhost

# Gamez port.
#gzport=8085

# Gamez uses ssl (0, 1).
#
# Set to 1 if using ssl, else set to 0.
#gzssl=0

# Gamez library
#
# move downloaded games here.
#gzlibrary

# Gamez web_root
#
# set this if using a reverse proxy.
#gzweb_root=

# Gamez and NZBGet are a different system (0, 1).
#
# Enable to replace local path with the path as per the mountPoints below.
#gzremote_path=0

## Network

# Network Mount Points (Needed for remote path above)
#
# Enter Mount points as LocalPath,RemotePath and separate each pair with '|'
# e.g. mountPoints=/volume1/Public/,E:\|/volume2/share/,\\NAS\
#mountPoints= 

## Extensions

# Media Extensions
#
# This is a list of media extensions that are used to verify that the download does contain valid media.
#mediaExtensions=.mkv,.avi,.divx,.xvid,.mov,.wmv,.mp4,.mpg,.mpeg,.vob,.iso

## Transcoder

# Transcode (0, 1).
#
# set to 1 to transcode, otherwise set to 0.
#transcode=0

# create a duplicate, or replace the original (0, 1).
#
# set to 1 to cretae a new file or 0 to replace the original
#duplicate=1

# set niceness level.
#
# Only works on Linux. Highest priority is -20, lowest priority is 19.
#niceness = 0

# ignore extensions.
#
# list of extensions that won't be transcoded.
#ignoreExtensions=.avi,.mkv

# outputFastStart (0,1).
#
# outputFastStart. 1 will use -movflags + faststart. 0 will disable this from being used.
#outputFastStart = 0

# outputVideoPath.
#
# outputVideoPath. Set path you want transcoded videos moved to. Leave blank to disable.
#outputVideoPath = 

# processOutput (0,1).
#
# processOutput. 1 will send the outputVideoPath to SickBeard/CouchPotato. 0 will send original files.
#processOutput = 0

# audioLanguage.
#
# audioLanguage. set the 3 letter language code you want as your primary audio track.
#audioLanguage = eng

# allAudioLanguages (0,1).
#
# allAudioLanguages. 1 will keep all audio tracks (uses AudioCodec3) where available.
#allAudioLanguages = 0

# subLanguages.
#
# subLanguages. create a list of languages in the order you want them in your subtitles. 
# (future versions I hope to support sub downlaod)
#subLanguages = eng,spa,fre

# allSubLanguages (0,1).
#
# allSubLanguages. 1 will keep all exisiting sub languages. 0 will discare those not in your list above.
#allSubLanguages = 0

# embedSubs (0,1).
#
# embedSubs. 1 will embded external sub/srt subs into your video if this is supported.
#embedSubs = 1

# burnInSubtitle (0,1).
#
# burnInSubtitle. burns the default sub language into your video (needed for players that don't support subs)
#burnInSubtitle = 0

# extractSubs (0,1).
#
# extractSubs. 1 will extract subs from the video file and save these as external srt files.
#extractSubs = 0

# externalSubDir.
#
# externalSubDir. set the directory where subs should be saved (if not the same directory as the video)
#externalSubDir =

# outputDefault (None, iPad, iPad-1080p, iPad-720p, Apple-TV2, iPod, iPhone, PS3, Roku-1080p, Roku-720p, Roku-480p).
#
# outputDefault. Loads default configs for the selected device. The remaining options below are ignored.
# If you want to use your own profile, set None and set the remaining options below.
#outputDefault = None

# ffmpeg output settings.
#outputVideoExtension=.mp4
#outputVideoCodec=libx264
#VideoCodecAllow = 
#outputVideoPreset=medium
#outputVideoFramerate=24
#outputVideoBitrate=800k
#outputAudioCodec=libmp3lame
#AudioCodecAllow = 
#outputAudioBitrate=128k
#outputQualityPercent = 0
#outputAudioTrack2Codec = libfaac
#AudioCodec2Allow = 
#outputAudioTrack2Bitrate = 128k
#outputAudioOtherCodec = libmp3lame
#AudioOtherCodecAllow = 
#outputAudioOtherBitrate = 128k
#outputSubtitleCodec =

## WakeOnLan

# use WOL (0, 1).
#
# set to 1 to send WOL broadcast to the mac and test the server (e.g. xbmc) on the host and port specified.
#wolwake=0

# WOL MAC
#
# enter the mac address of the system to be woken.
#wolmac=00:01:2e:2D:64:e1

# Set the Host and Port of a server to verify system has woken.
#wolhost=192.168.1.37
#wolport=80

### NZBGET POST-PROCESSING SCRIPT                                          ###
##############################################################################
import os
import sys
import datetime
import nzbtomedia
from nzbtomedia.autoProcess.autoProcessComics import autoProcessComics
from nzbtomedia.autoProcess.autoProcessGames import autoProcessGames
from nzbtomedia.autoProcess.autoProcessMovie import autoProcessMovie
from nzbtomedia.autoProcess.autoProcessMusic import autoProcessMusic
from nzbtomedia.autoProcess.autoProcessTV import autoProcessTV
from nzbtomedia.nzbToMediaUtil import getDirs, extractFiles, cleanDir, update_downloadInfoStatus, get_downloadInfo, CharReplace, convert_to_ascii
from nzbtomedia import logger, nzbToMediaDB

# post-processing
def process(inputDirectory, inputName=None, status=0, clientAgent='manual', download_id=None, inputCategory=None):
    if nzbtomedia.SAFE_MODE and inputDirectory == nzbtomedia.NZB_DEFAULTDIR:
        logger.error(
            'The input directory:[%s] is the Default Download Directory. Please configure category directories to prevent processing of other media.' % (
            inputDirectory))
        return -1

    if clientAgent != 'manual' and not nzbtomedia.DOWNLOADINFO:
        logger.debug('Adding NZB download info for directory %s to database' % (inputDirectory))

        myDB = nzbToMediaDB.DBConnection()

        encoded, inputDirectory1 = CharReplace(inputDirectory)
        encoded, inputName1 = CharReplace(inputName)

        controlValueDict = {"input_directory": unicode(inputDirectory1)}
        newValueDict = {"input_name": unicode(inputName1),
                        "input_hash": unicode(download_id),
                        "input_id": unicode(download_id),
                        "client_agent": unicode(clientAgent),
                        "status": 0,
                        "last_update": datetime.date.today().toordinal()
        }
        myDB.upsert("downloads", newValueDict, controlValueDict)

    # auto-detect section
    section = nzbtomedia.CFG.findsection(inputCategory).isenabled()
    if section is None:
        logger.error(
            'Category:[%s] is not defined or is not enabled. Please rename it or ensure it is enabled for the appropriate section in your autoProcessMedia.cfg and try again.' % (
            inputCategory))
        return -1

    if len(section) > 1:
        logger.error(
            'Category:[%s] is not unique, %s are using it. Please rename it or disable all other sections using the same category name in your autoProcessMedia.cfg and try again.' % (
            inputCategory, section.keys()))
        return -1

    if section:
        sectionName = section.keys()[0]
        logger.info('Auto-detected SECTION:%s' % (sectionName))
    else:
        logger.error("Unable to locate a section with subsection:%s enabled in your autoProcessMedia.cfg, exiting!" % (
            inputCategory))
        return -1

    try:
        extract = int(section[inputCategory]['extract'])
    except:
        extract = 0

    try:
        if int(section[inputCategory]['remote_path']) and not nzbtomedia.REMOTEPATHS:
            logger.error('Remote Path is enabled for %s:%s but no Network mount points are defined. Please check your autoProcessMedia.cfg, exiting!' % (
                sectionName, inputCategory))
            return -1
    except:
        logger.error('Remote Path %s is not valid for %s:%s Please set this to either 0 to disable or 1 to enable!' % (
            section[inputCategory]['remote_path'], sectionName, inputCategory))

    inputName, inputDirectory = convert_to_ascii(inputName, inputDirectory)

    if extract == 1:
        logger.debug('Checking for archives to extract in directory: %s' % (inputDirectory))
        extractFiles(inputDirectory)

    logger.info("Calling %s:%s to post-process:%s" % (sectionName, inputCategory, inputName))

    if sectionName == "CouchPotato":
        result = autoProcessMovie().process(sectionName, inputDirectory, inputName, status, clientAgent, download_id,
                                            inputCategory)
    elif sectionName in ["SickBeard", "NzbDrone"]:
        result = autoProcessTV().processEpisode(sectionName, inputDirectory, inputName, status, clientAgent,
                                                inputCategory)
    elif sectionName == "HeadPhones":
        result = autoProcessMusic().process(sectionName, inputDirectory, inputName, status, clientAgent, inputCategory)
    elif sectionName == "Mylar":
        result = autoProcessComics().processEpisode(sectionName, inputDirectory, inputName, status, clientAgent,
                                                    inputCategory)
    elif sectionName == "Gamez":
        result = autoProcessGames().process(sectionName, inputDirectory, inputName, status, clientAgent, inputCategory)
    else:
        result = -1

    if result == 0:
        if clientAgent != 'manual':
            # update download status in our DB
            update_downloadInfoStatus(inputName, 1)

        # cleanup our processing folders of any misc unwanted files and empty directories
        cleanDir(inputDirectory, sectionName, inputCategory)

    return result


def main(args, section=None):
    # Initialize the config
    nzbtomedia.initialize(section)

    # clientAgent for NZBs
    clientAgent = nzbtomedia.NZB_CLIENTAGENT

    logger.info("#########################################################")
    logger.info("## ..::[%s]::.. ##" % os.path.basename(__file__))
    logger.info("#########################################################")

    # debug command line options
    logger.debug("Options passed into nzbToMedia: %s" % args)

    # Post-Processing Result
    result = 0
    status = 0

    # NZBGet
    if os.environ.has_key('NZBOP_SCRIPTDIR'):
        # Check if the script is called from nzbget 11.0 or later
        if os.environ['NZBOP_VERSION'][0:5] < '11.0':
            logger.error("NZBGet Version %s is not supported. Please update NZBGet." %(str(os.environ['NZBOP_VERSION'])))
            sys.exit(nzbtomedia.NZBGET_POSTPROCESS_ERROR)

        logger.info("Script triggered from NZBGet Version %s." %(str(os.environ['NZBOP_VERSION'])))

        # Check if the script is called from nzbget 13.0 or later
        if os.environ.has_key('NZBPP_TOTALSTATUS'):
            if not os.environ['NZBPP_TOTALSTATUS'] == 'SUCCESS':
                logger.info("Download failed with status %s." %(os.environ['NZBPP_STATUS']))
                status = 1

        else:
            # Check par status
            if os.environ['NZBPP_PARSTATUS'] == '1' or os.environ['NZBPP_PARSTATUS'] == '4':
                logger.warning("Par-repair failed, setting status \"failed\"")
                status = 1

            # Check unpack status
            if os.environ['NZBPP_UNPACKSTATUS'] == '1':
                logger.warning("Unpack failed, setting status \"failed\"")
                status = 1

            if os.environ['NZBPP_UNPACKSTATUS'] == '0' and os.environ['NZBPP_PARSTATUS'] == '0':
                # Unpack was skipped due to nzb-file properties or due to errors during par-check

                if os.environ['NZBPP_HEALTH'] < 1000:
                    logger.warning(
                        "Download health is compromised and Par-check/repair disabled or no .par2 files found. Setting status \"failed\"")
                    logger.info("Please check your Par-check/repair settings for future downloads.")
                    status = 1

                else:
                    logger.info(
                        "Par-check/repair disabled or no .par2 files found, and Unpack not required. Health is ok so handle as though download successful")
                    logger.info("Please check your Par-check/repair settings for future downloads.")

        # Check for download_id to pass to CouchPotato
        download_id = ""
        if os.environ.has_key('NZBPR_COUCHPOTATO'):
            download_id = os.environ['NZBPR_COUCHPOTATO']

        # All checks done, now launching the script.
        clientAgent = 'nzbget'
        result = process(os.environ['NZBPP_DIRECTORY'], inputName=os.environ['NZBPP_NZBNAME'], status=status,
                         clientAgent=clientAgent, download_id=download_id, inputCategory=os.environ['NZBPP_CATEGORY'])
    # SABnzbd Pre 0.7.17
    elif len(args) == nzbtomedia.SABNZB_NO_OF_ARGUMENTS:
        # SABnzbd argv:
        # 1 The final directory of the job (full path)
        # 2 The original name of the NZB file
        # 3 Clean version of the job name (no path info and ".nzb" removed)
        # 4 Indexer's report number (if supported)
        # 5 User-defined category
        # 6 Group that the NZB was posted in e.g. alt.binaries.x
        # 7 Status of post processing. 0 = OK, 1=failed verification, 2=failed unpack, 3=1+2
        clientAgent = 'sabnzbd'
        logger.info("Script triggered from SABnzbd")
        result = process(args[1], inputName=args[2], status=args[7], inputCategory=args[5], clientAgent=clientAgent,
                         download_id='')
    # SABnzbd 0.7.17+
    elif len(args) >= nzbtomedia.SABNZB_0717_NO_OF_ARGUMENTS:
        # SABnzbd argv:
        # 1 The final directory of the job (full path)
        # 2 The original name of the NZB file
        # 3 Clean version of the job name (no path info and ".nzb" removed)
        # 4 Indexer's report number (if supported)
        # 5 User-defined category
        # 6 Group that the NZB was posted in e.g. alt.binaries.x
        # 7 Status of post processing. 0 = OK, 1=failed verification, 2=failed unpack, 3=1+2
        # 8 Failure URL
        clientAgent = 'sabnzbd'
        logger.info("Script triggered from SABnzbd 0.7.17+")
        result = process(args[1], inputName=args[2], status=args[7], inputCategory=args[5], clientAgent=clientAgent,
                         download_id='')
    else:
        # Perform Manual Post-Processing
        logger.warning("Invalid number of arguments received from client, Switching to manual run mode ...")

        for section, subsections in nzbtomedia.SECTIONS.items():
            for subsection in subsections:
                for dirName in getDirs(section, subsection):
                    logger.info("Starting manual run for %s:%s - Folder:%s" % (section, subsection, dirName))

                    logger.info("Checking database for download info for %s ..." % (os.path.basename(dirName)))
                    nzbtomedia.DOWNLOADINFO = get_downloadInfo(os.path.basename(dirName), 0)
                    if nzbtomedia.DOWNLOADINFO:
                        logger.info(
                            "Found download info for %s, setting variables now ..." % (os.path.basename(dirName)))
                    else:
                        logger.info(
                            'Unable to locate download info for %s, continuing to try and process this release ...' % (
                                os.path.basename(dirName))
                        )

                    try:
                        clientAgent = str(nzbtomedia.DOWNLOADINFO[0]['client_agent'])
                    except:
                        clientAgent = 'manual'
                    try:
                        download_id = str(nzbtomedia.DOWNLOADINFO[0]['input_id'])
                    except:
                        download_id = None

                    if clientAgent.lower() not in nzbtomedia.NZB_CLIENTS and clientAgent != 'manual':
                        continue

                    results = process(dirName, os.path.basename(dirName), 0, clientAgent=clientAgent,
                                      download_id=download_id, inputCategory=subsection)
                    if results != 0:
                        logger.error("A problem was reported when trying to perform a manual run for %s:%s." % (
                        section, subsection))
                        result = results

    if result == 0:
        logger.info("The %s script completed successfully." % args[0])
        if os.environ.has_key('NZBOP_SCRIPTDIR'):  # return code for nzbget v11
            return (nzbtomedia.NZBGET_POSTPROCESS_SUCCESS)
    else:
        logger.error("A problem was reported in the %s script." % args[0])
        if os.environ.has_key('NZBOP_SCRIPTDIR'):  # return code for nzbget v11
            return (nzbtomedia.NZBGET_POSTPROCESS_ERROR)

    return (result)


if __name__ == '__main__':
    exit(main(sys.argv))
