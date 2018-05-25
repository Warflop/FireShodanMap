# FireShodanMap
FireShodanMap is a Realtime map that integrates [Firebase](https://firebase.google.com/) and [Shodan](https://www.shodan.io). A search is carried out using Shodan searching vulnerable devices and they are showed on the map for analysis. All data updated in Firebase are Realtime.

![ScreenShot](https://raw.githubusercontent.com/Warflop/FireShodanMap/master/screenshot.png)

# Changes

We have a file named "fireshodan.py" responsible for fill Firebase database, we need to change:

<pre>
[+] <b>FILE_WITH_KEY.json</b> (Open the Credentials tab and click <b>Create credentials</b>. You want the API key option. Create a server key. It will automatically download as a *.json file)
[+] <b>KEY_FIREBASE_HERE</b> (Open the Firebase Project and click <b>Add Firebase to your web application</b>)
[+] <a href="https://account.shodan.io/">API_SHODAN_KEY</a>
</pre>

Now, we need to change **index.html** and **firebase_conf.js** files.

<pre>
[+] index.html - <a href="https://developers.google.com/maps/documentation/javascript/get-api-key?hl=en">MY_KEY_MAP</a>
[+] firebase_conf.js - Open the Firebase Project and click <b>Add Firebase to your web application</b>
</pre>
# Usage Example
<pre>
Access index.html file and run "python fireshodan.py" to fill your database. 
You can see your data now. If you remove any data your map will update automatic.
<b>OBS: If you stop the script the data will continue there</b>
</pre>
# Greetz
<pre>
<a href="https://github.com/netoolii">Neto Oliveira</a>
<a href="https://github.com/AleBarreto">Alessandro Barreto</a>
<a href="https://github.com/GabrielCarneiroDeveloper">Gabriel Carneiro</a>
</pre>
