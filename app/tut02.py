import random
import string
import cherrypy
import time
import io
import os


import sys
sys.path.insert(0, '../analytics')
from analytics import test, main
from input import upload_audio

BUCKET_NAME = 'rover1'
CREDENTIALS = '../credentials/RoverApp-2c2a3600d6d9.json'

class StringGenerator(object):

    @cherrypy.expose
    def index(self):

        return """<html>
        <head>
        <title>Rover</title>
        <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script>
        <script type = "text/javascript">

        

        function buttonFunction() {
          document.getElementById('button1').style.background = "#73A9BF";
          document.getElementById('button1').style.color = "#EEF4F7";
          document.getElementById('button1').innerHTML = "<b>STOP RECORDING</b>";
          document.getElementById('button1').setAttribute( "onClick", "javascript: buttonFunctionTwo();" );
        }
        function buttonFunctionTwo() {
          document.getElementById('button1').style.background = "#FFFFFF";
          document.getElementById('button1').style.color = "#48859D";
          document.getElementById('button1').innerHTML = "<b>RECORD AUDIO</b>";
          document.getElementById('button1').setAttribute( "onClick", "javascript: buttonFunction();" );

          window.location = "pagethree";
        }

        

        </script>
        <style>
        @import url('https://fonts.googleapis.com/css?family=Questrial');
        </style>
        <style type = "text/css">

        body {
          background: linear-gradient(#CBDFE7, #96BFCF);
          font-family: 'Questrial';
        }

        h1 {
          color: #284A57;
          text-align: center;
          font-size: 1500%;
          margin-top: 5%;
          padding-bottom: 4%;

        }

        h2 {
          color: #284A57;
          text-align: center;
          margin-top: -15%;
          font-size: 300%
        }

        button {
          background-color: #FFFFFF;
          color: #48859D;
          border: none;
          padding: 15px 32px;
          display: block;
          margin: 0 auto;
          font-size: 200%;


        }

        form {
        margin: 0 auto;
        text-align: center;
        }

        input[type=button], input[type=submit], input[type=reset] {

        }

        </style>
        </head>
        <body id="bod">
        <h1 id="one"><b>ROVER</b></h1>
        <h2 id="two">It's like Shazam... for scholars!</h2>
        <button id="button1" onclick="buttonFunction()"><b>RECORD AUDIO</b></button><br>
        <form action="upload" method="post" enctype="multipart/form-data" id="form1">
        <input type="file" name="myFile"/><br />
        <input type="submit"/>
        </form>
        </body>
        </html>
"""


    @cherrypy.expose
    def pagethree(self):
        variable = self.variable

        titlea = variable[0][0]
        titleb = variable[1][0]
        titlec = variable[2][0]
        authora = variable[0][1]
        authorb = variable[1][1]
        authorc = variable[2][1]
        abstracta = variable[0][2]
        abstractb = variable[1][2]
        abstractc = variable[2][2]
        linka = variable[0][3]
        linkb = variable[1][3]
        linkc = variable[2][3]

        return """<html>
        <head>
        <title>Rover</title>

        <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script>
        <script type = "text/javascript">
        </script>

        <script language = "javascript">

        $( document ).ready(function() {
        $('html, body').animate({ scrollTop: $(document).height() }, 1200);
        });

        function buttonFunction() {
          document.getElementById('button1').style.background = "#73A9BF";
          document.getElementById('button1').style.color = "#EEF4F7";
          document.getElementById('button1').innerHTML = "<b>STOP RECORDING</b>";
          document.getElementById('button1').setAttribute( "onClick", "javascript: buttonFunctionTwo();" );
        }
        function buttonFunctionTwo() {
          document.getElementById('button1').style.background = "#FFFFFF";
          document.getElementById('button1').style.color = "#48859D";
          document.getElementById('button1').innerHTML = "<b>RECORD AUDIO</b>";
          document.getElementById('button1').setAttribute( "onClick", "javascript: buttonFunction();" );
          window.location = "pagethree";
        }

        </script>

        <style>
        @import url('https://fonts.googleapis.com/css?family=Questrial');
        </style>
        <style type = "text/css">

        body {
          background: linear-gradient(#CBDFE7, #96BFCF);
          background-attachment: fixed;
          font-family: 'Questrial';
        }

        h1 {
          color: #284A57;
          text-align: center;
          font-size: 1500%;
          margin-top: 5%;
          padding-bottom: 4%;

        }

        h2 {
          color: #284A57;
          text-align: center;
          margin-top: -15%;
          font-size: 300%
        }
        h3 {
          color: #284A57;
          text-align: center;
          font-size: 300%;
          margin-top: 20%;
        }

        button {
          background-color: #FFFFFF;
          color: #48859D;
          border: none;
          padding: 15px 32px;
          display: block;
          margin: 0 auto;
          font-size: 200%;

          font-family: 'Questrial';
        }

        h2 {
          color: #284A57;
          text-align: center;
          font-size: 300%;
          margin-top: 5%;
        }

        .art {
          background-color: #FFFFFF;
          width: 70%;
          height: 20%;
          margin: 20px 20px 20px 20px;
          margin-bottom: 3%;
          margin: 0 auto;

        }

        .t {
          text-align: center;
          padding-top: 2%;
          margin-top: 3%;
          font-size: 150%;
          color: #48859D;
          padding-bottom: 1%;
        }

        .author {

            font-size: 80%;
            text-align: center;

        }

        .a {
            padding: 20px 20px 20px 20px;
            margin-top: -1%;
        }

        .block {
        margin-bottom: 5%;
        }

        a {
        color: inherit; /* blue colors for links too */
        text-decoration: inherit; /* no underline */
        }

        </style>
        </head>
        <body id="bod">
        <h1 id="one"><b>ROVER</b></h1>
        <h2 id="two">It's like Shazam... for scholars!</h2>
        <button id="button1" onclick="buttonFunction()"><b>RECORD AUDIO</b></button>
        <form action="upload" method="post" enctype="multipart/form-data" id="form1">
        <input type="file" name="myFile"/><br />
        <input type="submit"/>
        <h3 id="three">ARTICLES</h3>
        <div class = block>
        <div class = article><a href='"""+linka+"""'><div class = art><div class = t><b>"""+titlea+"""</b></div><div class = author>"""+authora+"""</div><div class = a>"""+abstracta+"""</div></a></div>
        <div class = article><a href='"""+linkb+"""'><div class = art><div class = t><b>"""+titleb+"""</b></div><div class = author>"""+authorb+"""</div><div class = a>"""+abstractb+"""</div></a></div>
        <div class = article><a href='"""+linkc+"""'><div class = art><div class = t><b>"""+titlec+"""</b></div><div class = author>"""+authorc+"""</div><div class = a>"""+abstractc+"""</div></a></div></div>
        </body>
        </html>
        """

    @cherrypy.expose
    def upload(self, myFile):
        file_name = 'f' + str(int(time.time())) + '.flac'
        write_file = io.open(file_name, 'wb')
        while True:
            data = myFile.file.read(8192)
            write_file.write(data)
            if not data:
                break
        write_file.close()

        upload_audio(CREDENTIALS, BUCKET_NAME, file_name)
        os.remove(file_name)
        # time.sleep(30)

        self.variable = main(BUCKET_NAME, file_name, 44100, 0)

        return self.pagethree()


if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator())
