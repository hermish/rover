import random
import string
import cherrypy

class StringGenerator(object):
    @cherrypy.expose
    def index(self):

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
    def pagethree(self):
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
        <h3 id="three">ARTICLES</h3>
        <div class = block>
        <div class = article><a href="http://facebook.com"><div class = art><div class = t><b>Title A</b></div><div class = author>AUTHOR NAME</div><div class = a>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id.</div></a></div>
        <div class = article><a href="http://facebook.com"><div class = art><div class = t><b>Title B</b></div><div class = author>AUTHOR NAME</div><div class = a>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id.</div></a></div>
        <div class = article><a href="http://facebook.com"><div class = art><div class = t><b>Title C</b></div><div class = author>AUTHOR NAME</div><div class = a>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id.</div></a></div></div>
        </body>
        </html>
        """

        #titlea = variable[0][0]
        #titleb = variable[1][0]
        #titlec = variable[2][0]
        #authora = variable[0][1]
        #authorb = variable[1][1]
        #authorc = variable[2][1]
        #abstracta = variable[0][2]
        #abstractb = variable[1][2]
        #abstractc = variable[2][2]
        #linka = variable[0][3]
        #linkb = variable[1][3]
        #linkc = variable[2][3]




if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator())
