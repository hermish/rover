import random
import string
from analytics import test
import cherrypy


class StringGenerator(object):
    @cherrypy.expose
    def pageone(self):

        return """<html>
        <head>
        <title>Rover</title>
        <script language = "javascript">

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
          window.location = "pagetwo";
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
          font-size: 2000%;
          margin-top: 5%;

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

        </style>
        </head>
        <body id="bod">
        <h1 id="one"><b>ROVER</b></h1>
        <h2 id="two">It's like Shazam... for scholars!</h2>
        <button id="button1" onclick="buttonFunction()"><b>RECORD AUDIO</b></button>
        </body>
        </html>
"""

    @cherrypy.expose
    def pagetwo(self):

        result_list = test()

        return """<html>
        <head>
        <title>Rover</title>
        <style>
        @import url('https://fonts.googleapis.com/css?family=Questrial');
        </style>
        <style type = "text/css">

        body {
          background: linear-gradient(#CBDFE7, #96BFCF);
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
          box-shadow: 2px 2px 10px #38687A;
          margin: 0 auto;

        }

        .t {
          text-align: center;
          padding-top: 2%;
          margin-top: 3%;
          font-size: 200%;
          color: #48859D;
        }

        </style>
        </head>

        <body id="bod">
        <h2 id="two">ARTICLES</h2>
        <div class = article><div class = art><div class = t><b>""" + result_list[0][0] + """</b></div></div></div>
        <div class = article><div class = art><div class = t><b>""" + result_list[1][0] + """</b></div></div></div>
        <div class = article><div class = art><div class = t><b>""" + result_list[2][0] + """</b></div></div></div>

        </body>
        </html>
"""



if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator())
