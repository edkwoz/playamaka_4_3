from flask import Flask, render_template, request, session
from forms import SupaPlayaMaka
# from KalturaClient import *
# from KalturaClient.Plugins.Core import *
import requests, json, os
from ftplib import FTP


app = Flask(__name__)
app.secret_key = "TEST"


# @app.route('/writeftp', methods=['GET', 'POST'])
# def writeftp():
#     return
    # text = 'Sample text to save\nNew line!'
    # saveFile = open('examplefile.txt', 'w')
    # saveFile.write(text)=
    # saveFile.close()
    #
    # path = "~/Desktop/UPLOADS/slideshow"
    # path = os.path.expanduser(path)
    # os.chdir(path)
    # retval2 = os.getcwd()
    # files = os.listdir(path)
    #
    # ftp = FTP('webdev.bu.edu')
    # ftp.login(user='video', passwd='OnlineBU1960')
    # ftp.cwd('html_swf_previews/PUBLIC/01_FTP_PLAYLIST_TEST/')
    #
    # x = 0
    #
    # for f in files:
    #     if os.path.isfile(path):
    #         fh = open(f, 'rb')
    #         ftp.storbinary('STOR %s' % f, fh)
    #         fh.close()
    #         x += 1
    #     elif os.path.isdir(path):
    #         ftp.mkd(f)
    #         ftp.cwd(f)
    #         uploadThis(path)
    #         x += 1
    # ftp.cwd('..')
    # os.chdir('..')
    # return render_template('ftp_test_complete.html', retval2=retval2, files=files, x=x)

    # for f in files:
    #     if f == '.DS_Store':
    #         pass
    #     elif os.path.isdir(path):
    #         x = 5
    #         ftp.mkd(f)
    #         return render_template('ftp_test_complete.html', retval2=retval2, files=files, x=x)
    #
    #     ftp = FTP('webdev.bu.edu')
    #     ftp.login(user='video', passwd='OnlineBU1960')
    #     ftp.cwd('html_swf_previews/PUBLIC/01_FTP_PLAYLIST_TEST/')
    #
    #     if os.path.isfile(path + r'\{}'.format(f)):
    #         fh = open(f, 'rb')
    #         ftp.storbinary('STOR %s' % f, fh)
    #         fh.close()
    #     elif os.path.isdir(path + r'\{}'.format(f)):
    #         ftp.mkd(f)
    #         ftp.cwd(f)
    #         uploadThis(path + r'\{}'.format(f))
    #     else:
    #         pass
    # ftp.cwd('..')
    # os.chdir('..')

    # return render_template('ftp_test_complete.html', retval2=retval2, files=files)

    # ftp = FTP('webdev.bu.edu')
    # ftp.login(user='video', passwd='OnlineBU1960')
    # ftp.cwd('html_swf_previews/PUBLIC/01_FTP_PLAYLIST_TEST/')

    # files = os.listdir(path)
#     os.chdir(path)
#     for f in files:
#         if os.path.isfile(path + r'\{}'.format(f)):
#             fh = open(f, 'rb')
#             myFTP.storbinary('STOR %s' % f, fh)
#             fh.close()
#         elif os.path.isdir(path + r'\{}'.format(f)):
#             myFTP.mkd(f)
#             myFTP.cwd(f)
#             uploadThis(path + r'\{}'.format(f))
#     myFTP.cwd('..')
#     os.chdir('..')
# uploadThis(myPath) # now call the recursive function
#
#
#
#     filename = 'slideshow'
#     if filename in ftp.nlst():
#         return render_template('file_exists.html')
#     else:
#         ftp.storbinary('STOR ' + filename, open(filename, 'rb'))
#         ftp.quit()






@app.route('/', methods=['GET', 'POST'] )
def index():
    return render_template('index.html')



###########
#controller gets the number of files you want to enter, before going to type in the file names
@app.route('/howmany', methods=['GET', 'POST'] )
def howmany():
    form = SupaPlayaMaka()
    return render_template('howmany.html', form=form)



###########
#controller gets the number of files you want to enter, before going to type in the file names
@app.route('/howmany_AD', methods=['GET', 'POST'] )
def howmany_AD():
    form = SupaPlayaMaka()
    return render_template('howmany_AD.html', form=form)



###########
#controller makes text inputs based on the number entered in howmany
@app.route('/enterfiles', methods=['GET', 'POST'] )
def enterfiles():
    form = SupaPlayaMaka()
    numfiles = request.form.get('amount')
    numfilesint = int(numfiles)
    session['x'] = 1
    return render_template('enterfiles.html',form=form, numfilesint=numfilesint)


###########
#controller makes text inputs based on the number entered in howmany
@app.route('/enterfiles_AD', methods=['GET', 'POST'] )
def enterfiles_AD():
    form = SupaPlayaMaka()
    numfiles = request.form.get('amount')
    numfilesint = int(numfiles)
    session['x'] = 1
    return render_template('enterfiles_AD.html',form=form, numfilesint=numfilesint)



###########
#controller allows files to be input for video names to playeropts
@app.route('/selectfiles', methods=['GET', 'POST'] )
def selectfiles():
    form = SupaPlayaMaka()
    playa_option = request.form['playerchoice']
    session['player_option'] = playa_option
    session['x'] = 0
    return render_template('selectfiles.html', form=form)



###########
#controller makes form for selecting player type
@app.route('/playeropts1', methods=['GET', 'POST'] )
def playeropts1():
    form = SupaPlayaMaka()
    return render_template('playeropts1.html', form=form)



###########
#controller takes file names from selectfiles or enterfiles and goes to entry ids
@app.route('/entryids', methods=['GET', 'POST'] )
def entryids():
    form = SupaPlayaMaka()
    x = session.get('x', None)
    if x == 0:
        files = request.form.getlist('videofile')
        newfiles = []
        for f in files:
            newf = os.path.splitext(f)[0]
            newfiles.append(newf)
        session['file_var'] = newfiles
        return render_template('entryids.html', form=form, newfiles=newfiles)
    else:
        files = request.form.getlist('filename')
        newfiles = []
        for f in files:
            newfiles.append(f)
        session['file_var'] = newfiles
        return render_template('entryids.html', form=form, newfiles=newfiles)




###########
#controller takes file names from selectfiles or enterfiles and goes to entry ids
@app.route('/entryids_AD', methods=['GET', 'POST'] )
def entryids_AD():
    form = SupaPlayaMaka()
    x = session.get('x', None)
    if x == 0:
        files = request.form.getlist('videofile')
        newfiles = []
        for f in files:
            newf = os.path.splitext(f)[0]
            newfiles.append(newf)
        session['file_var'] = newfiles
        return render_template('entryids_AD.html', form=form, newfiles=newfiles)
    else:
        files = request.form.getlist('filename')
        newfiles = []
        for f in files:
            newfiles.append(f)
        session['file_var'] = newfiles
        return render_template('entryids_AD.html', form=form, newfiles=newfiles)



###########
#controller takes file names, entry ids, and player option and outputs code
@app.route('/codeout', methods=['GET', 'POST'] )
def codeout():
    player_option = session.get('player_option', None)
    files = session.get('file_var', None)
    length = len(files)
    entryids = request.form.getlist('entryid')
    if player_option == 'standardplayer':
        return render_template('standardplayer.html', files=files, entryids=entryids, length=length)
    else:
        return render_template('audioplayer.html', files=files, entryids=entryids, length=length)


###########
#controller takes file names, entry ids, and player option and outputs code
@app.route('/codeout_AD', methods=['GET', 'POST'] )
def codeout_AD():
    files = session.get('file_var', None)
    length = len(files)
    entryids = request.form.getlist('entryid')
    file_idlist = []
    for f in files:
        caption_filename = f
        url_g = 'http://api.3playmedia.com/files?apikey=qPkBhpMQzvvZFJqbAw5MgaWwVMmUZtRX&q=name=%s' % caption_filename
        g = requests.get(url_g)
        response = g.text
        listofdicts = json.loads(response)
        dictchoice = listofdicts['files']
        finaldict = dictchoice[0]

        for key, value in finaldict.items():
            if key == 'id':
                file_id = value
                break
            else:
                continue

        file_idlist.append(file_id)
    return render_template('audio_description.html', files=files, entryids=entryids, length=length, file_idlist=file_idlist, listofdicts=listofdicts, dictchoice=dictchoice, finaldict=finaldict)




###########
#controller takes file names, entry ids, and player option and outputs code with duration from Kaltura API
# @app.route('/codeout', methods=['GET', 'POST'] )
# def codeout():
#     #sets up Kaltura API session
#     partnerId = 2159741
#     config = KalturaConfiguration(2159741)
#     config.serviceUrl = "https://admin.kaltura.com/"
#     client = KalturaClient(config)
#     secret = "2cdc6c22340f7e42345e3f7883d7c354"
#     userId = "video@bu.edu"
#     ktype = KalturaSessionType.ADMIN
#     expiry = 432000 # 432000 = 5 days
#     privileges = "disableentitlement"
#
#     #gets player type, file names, length of files and entryids from all previous forms
#     player_option = session.get('player_option', None)
#     files = session.get('file_var', None)
#     length = len(files)
#     entryids = request.form.getlist('entryid')
#
#     durations = []
#
#     #make api calls to get duration of each videos
#     for e in entryids:
#         #start api session
#         ks = client.session.start(secret, userId, ktype, partnerId, expiry, privileges)
#         client.setKs(ks)
#         result = client.media.get(e)
#         t = result.duration
#         durations.append(t)
#
#     if player_option == 'standardplayer':
#         return render_template('standardplayer.html', files=files, entryids=entryids, length=length, durations=durations)
#     else:
#         return render_template('audioplayer.html', files=files, entryids=entryids, length=length)




###########
#controller gets file inputs for making slideshow
# @app.route('/slideshow', methods=['GET', 'POST'] )
# def slideshow():
#     form = SupaPlayaMaka()
#     return render_template('slidefiles.html', form=form)



###########
#controller takes file names from selectfiles or enterfiles and goes to entry ids
# @app.route('/slideplayer', methods=['GET', 'POST'] )
# def slideplayer():
#     form = SupaPlayaMaka()
#     slideshowfolder = request.form.get('slideshowfolder')
#     session['slideshowfolder'] = slideshowfolder
#     college = request.form.get('college')
#     course = request.form.get('course')
#     files = request.form.getlist('slidefile')
#     length = len(files)
#     height = request.form.get('height')
#     width = request.form.get('width')
#     fadeopt = request.form.get('fadeopt')
#     path = "~/Desktop/UPLOADS/" + slideshowfolder
#     path = os.path.expanduser(path)
#     os.chdir(path)
#
#     data1 =  """
#     <!DOCTYPE html>
#     <html>
#     <head>
#     <meta name="viewport" content="width=device-width, initial-scale=1">
#     <title>Slideshow</title>
#     <style>
#     * {box-sizing:border-box}
#     body {font-family: Verdana,sans-serif;margin:0}
#     .mySlides {display:none}
#
#     .slideshow-container {
#     max-width: %spx;
#     max-height: %spx;
#     position: relative;
#     margin: auto;
#     }
#
#     .prev, .next {
#     cursor: pointer;
#     position: absolute;
#     top: 50%%;
#     width: auto;
#     padding: 16px;
#     margin-top: -22px;
#     color: white;
#     background-color: rgba(0, 0, 0, 0.5);
#     font-weight: bold;
#     font-size: 18px;
#     transition: 0.6s ease;
#     border-radius: 0 3px 3px 0;
#     }
#
#     .next {
#     right: 0;
#     border-radius: 3px 0 0 3px;
#     }
#
#     .prev:hover, .next:hover {
#     background-color: rgba(0,0,0,1.0);
#     }
#
#     .numbertext {
#     color: #ffffff;
#     font-size: 12px;
#     padding: 8px 12px;
#     position: absolute;
#     top: 0;
#     background-color: rgba(0, 0, 0, 0.8);
#     }
#
#     img {
#     width: %spx;
#     height: %spx;
#     }
#
#     .dot {
#     cursor:pointer;
#     height: 10px;
#     width: 10px;
#     margin: 0 2px;
#     background-color: #bbb;
#     border-radius: 50%%;
#     display: inline-block;
#     transition: background-color 0.6s ease;
#     }
#
#     .active, .dot:hover {
#     background-color: #717171;
#     }
#     """ % (width, height, width, height)
#
#     if fadeopt:
#         data2withfade = """
#         .fade {
#           -webkit-animation-name: fade;
#           -webkit-animation-duration: 1.5s;
#           animation-name: fade;
#           animation-duration: 1.5s;
#         }
#
#         @-webkit-keyframes fade {
#           from {opacity: .4}
#           to {opacity: 1}
#         }
#
#         @keyframes fade {
#           from {opacity: .4}
#           to {opacity: 1}
#         }
#         """
#     else:
#         data2withfade = ""
#
#     data2afterfade = """
#     @media only screen and (max-width: 300px) {
#       .prev, .next,.text {font-size: 11px}
#     }
#
#     </style>
#     </head>
#     <body>
#
#     <div class="slideshow-container">
#     """
#
#     data3for = ""
#     for i in range (0, length):
#         file = files[i]
#         data3for += """<div class="mySlides fade">
#         <div class="numbertext">%s / %s</div>
#         <img src="img/%s" style="width:100%%">
#         </div>
#         """ % (i+1, length, file)
#
#     data4 = """<a class="prev" onclick="plusSlides(-1)">&#10094;</a>
#     <a class="next" onclick="plusSlides(1)">&#10095;</a>
#
#     </div>
#
#     <div style="text-align:center">"""
#
#     data5for = ""
#     for i in range (0, length):
#         data5for += """<span class="dot" onclick="currentSlide(%s)"></span>""" % (i+1)
#
#     data6 = """</div>
#
#     <script>
#     var slideIndex = 1;
#     showSlides(slideIndex);
#
#     function plusSlides(n) {
#     showSlides(slideIndex += n);
#     }
#
#     function currentSlide(n) {
#     showSlides(slideIndex = n);
#     }
#
#     function showSlides(n) {
#     var i;
#     var slides = document.getElementsByClassName("mySlides");
#     var dots = document.getElementsByClassName("dot");
#     if (n > slides.length) {slideIndex = 1}
#     if (n < 1) {slideIndex = slides.length}
#     for (i = 0; i < slides.length; i++) {
#         slides[i].style.display = "none";
#     }
#     for (i = 0; i < dots.length; i++) {
#         dots[i].className = dots[i].className.replace(" active", "");
#     }
#     slides[slideIndex-1].style.display = "block";
#     dots[slideIndex-1].className += " active";
#     }
#     </script>
#
#     </body>
#     </html>"""
#
#
#     previewdata1 = """
#     <!DOCTYPE html>
#     <html>
#     <head>
#     <meta name="viewport" content="width=device-width, initial-scale=1">
#     <title>Slideshow Embed Code</title>
#     </head>
#     <body>
#     <p>&nbsp;</p>
#     <h3>%s</h3>
#
#     <div>
#     <object id="%s" type="text/html" width="%s" height="%s" data="https://www.bu.edu/av/disted/html_swf_previews/MEDIA_OBJECTS/%s/%s/%s/index.html">
#     </object>
#     </div>
#     <div>
#     <textarea cols="200" rows="5">
#     <object id="%s" type="text/html" width="%s" height="%s" data="https://www.bu.edu/av/disted/html_swf_previews/MEDIA_OBJECTS/%s/%s/%s/index.html">
#     </object>
#     </textarea>
#     </div>
#     <p>&nbsp;</p>
#
#     </body>
#
#     </html>
#         """ % (slideshowfolder, slideshowfolder, width, height, college, course, slideshowfolder, slideshowfolder, width, height, college, course, slideshowfolder)
#
#     with open("index.html","w") as fo:
#         fo.write(data1 + data2withfade + data2afterfade + data3for + data4 + data5for + data6)
#     with open("preview.html","w") as fo:
#         fo.write(previewdata1)
#
#     return render_template('slideshowcomplete.html', slideshowfolder=slideshowfolder, college=college, course=course)

    # os.chdir('..')

    # file = "index.html"
    #
    # newpath = "html_swf_previews/MEDIA_OBJECTS/%s/%s/slide/" % (college, course)
    # ftp = FTP('webdev.bu.edu')
    # ftp.login(user='video', passwd='OnlineBU1960')
    # ftp.cwd(newpath)
    # ftp.storbinary('STOR '+file, open(file, 'rb'))
    # ftp.quit()










    # ftp.storbinary('STOR '+file, open(file, 'rb'))
    # ftp.quit()








    # for f in files:
    #     if os.path.isfile(path):
    #         fh = open(f, 'rb')
    #         ftp.storbinary('STOR %s' % f, fh)
    #         fh.close()
    #     else:
    #         continue
    # ftp.cwd('..')
    # os.chdir('..')
    # ftp.quit()

    # return render_template('slideplayertesting.html', form=form, height=height, width=width, fadeopt=fadeopt, file=file)



###########
#controllers fill video id field in 3play for captions
@app.route('/captions1', methods=['GET', 'POST'] )
def captions1():
    form = SupaPlayaMaka()
    if request.method == 'POST':
        return redirect(url_for('captions2'))
    elif request.method == 'GET':
        return render_template('captions1.html', form=form)

@app.route('/captions2', methods=['GET', 'POST'] )
def captions2():
    form = SupaPlayaMaka()
    # gets files from form
    files = request.form.getlist('captionfile')
    # strips the file extension from the file input and makes new list
    newfiles = []
    for f in files:
        newf = os.path.splitext(f)[0]
        newfiles.append(newf)

    # issues get request to 3play api to get the id# of the named file
    file_idlist = []
    for f in newfiles:
        caption_filename = f
        url_g = 'http://api.3playmedia.com/files?apikey=qPkBhpMQzvvZFJqbAw5MgaWwVMmUZtRX&q=name=%s' % caption_filename
        g = requests.get(url_g)
        response = g.text
        listofdicts = json.loads(response)
        dictchoice = listofdicts['files']
        finaldict = dictchoice[0]

        for key, value in finaldict.items():
            if key == 'id':
                file_id = value
                break
            else:
                continue

        file_idlist.append(file_id)

    # issues the put request, using the id# to populate the video id
    i = 0
    for f in newfiles:
        caption_filename = f
        file_id = file_idlist[i]
        url_p = 'http://api.3playmedia.com/files/%s' % file_id
        params_p = {'apikey':'qPkBhpMQzvvZFJqbAw5MgaWwVMmUZtRX', 'api_secret_key':'dMkGa_CVlIjL8clh3I3bPfH0EQrgp_w7', '_method':'PUT', 'video_id':'%s' % caption_filename}
        p = requests.put(url_p, params=params_p)
        i += 1

    return render_template('captions2.html', newfiles=newfiles)




if __name__ == "__main__":
  app.run(debug=False)
