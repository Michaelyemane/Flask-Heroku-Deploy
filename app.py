from flask import Flask, render_template
from string import Template
import os

app = Flask(__name__)

HTML_TEMPLATE = Template("""
<DOCTYEP html>
  <html lang="en">
      <head>
          <meta charset="UTF-8">
          <meta http-equiv="X-UA-Compatible" content="IE=edge">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>Ethio-TV & Radio</title>

          <script src="https://cdn.jsdelivr.net/npm/hls.js@latest">
            {*{
                    margin: 0; padding:0;
                    box-sizing: border-box;
                    text-transform: capitalize;
                    font-family: Verdana, Geneva, Tahoma, sans-serif;
                    font-weight: normal;
                }

            .body{
                    background: #eee;
                }

            .heading{
                    color: #444;
                    font-size: 40px;
                    text-align: center;
                    padding: 10px;
                }

            .container{
                    display: grid;
                    grid-template-columns: 1fr;
                    gap: 15px;
                    align-items: flex-start;
                    padding: 5px 5%;
                }

            .container .main-video video{
                    width: 100%;
                    border-radius: 5px;
                }

            @media (max-width:991px){
                    .container{
                    grid-template-columns: 1.5fr 1fr;
                    padding: 10px;
                    }
                }

            @media (max-width:768px){
                    .container{
                    grid-template-columns: 1fr;
                    }
                }}
          </script>
          
      </head>
      <body background="Static/bg.png">
        <Center>
            <h3 class="heading">${place_holder}</h3>
        </center
        <div class="container">
            <center>
            <div class="main-video">
                <div class="video">
                    <video id="video" controls autoplay></video>
                </div>
            </div>
            </center>
        </div>

        <script>
            if(Hls.isSupported())
                    {
                        var video = document.getElementById('video');
                        var hls = new Hls();
                        hls.loadSource('https://${place_name}');
                        hls.attachMedia(video);
                        hls.on(Hls.Events.MANIFEST_PARSED,function()
                        {
                            Video.play();
                        });
                    }
                    else if (video.canPlayType('application/vnd_apple_mpegurl'))
                    {
                        video.src = 'https://${place_name}';
                        video.addEventListener('canplay',function()
                        {
                            video.play();
                        });
                    }
        </script>

      </body>
  </html>
""")

HTML_TEMPLATE_2 = Template("""
<DOCTYEP html>
  <html lang="en">
      <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>Ethio-TV & Radio</title>
      </head>
      <body background="Static/bg.png">
        <div class="Audio">
            <center>
                <h2>${place_holder2}</h2>
                <audio src="https://${place_name}" controls="true" volume="1.0" __idm_id__="1712129"></audio>
              </center>
        </div>
                
      </body>
      
  </html>
""")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tv')
def tv():
    return render_template('live_tv.html')

#---------TV-------------------------------
@app.route('/addis_media_network')
def addis_media_network():
    return (HTML_TEMPLATE.substitute(place_holder='ADDIA MEDIA TV', place_name='player.mayya.et/play/d0019c9d-5088-47a2-bb9a-ec5fff5b9b4a/addis_1_480p/index.m3u8'))

@app.route('/amhara_media_corporation_1')
def amhara_media_corporation_1():
    return(HTML_TEMPLATE.substitute(place_holder='AMHARA TV 1', place_name='player.mayya.et/play/b83319a5-ac2b-4fcb-889e-38aaafc50f4f/AsyZVK5qWWBn_480p/index.m3u8'))

@app.route('/amhara_media_corporation_2')
def amhara_media_corporation_2():
    return(HTML_TEMPLATE.substitute(place_holder='AMHARA TV 2', place_name='player.mayya.et/play/b83319a5-ac2b-4fcb-889e-38aaafc50f4f/amhara-hiber_1_src/index.m3u8'))

@app.route('/arts_tv')
def arts_tv():
    return(HTML_TEMPLATE.substitute(place_holder='ARTS TV', place_name='player.mayya.et/play/d0019c9d-5088-47a2-bb9a-ec5fff5b9b4a/arts_1_480p/index.m3u8'))

@app.route('/asham_tv')
def asham_tv():
    return(HTML_TEMPLATE.substitute(place_holder='ASHAM TV', place_name='player.mayya.et/play/d0019c9d-5088-47a2-bb9a-ec5fff5b9b4a/asham_1_480p/index.m3u8'))

@app.route('/balageru_tv')
def balageru_tv():
    return(HTML_TEMPLATE.substitute(place_holder='BALAGERU TV', place_name='player.mayya.et/play/d0019c9d-5088-47a2-bb9a-ec5fff5b9b4a/balageru_1_480p/index.m3u8'))

@app.route('/ebs_tv')
def ebs_tv():
    return(HTML_TEMPLATE.substitute(place_holder='EBS TV', place_name='player.mayya.et/play/d0019c9d-5088-47a2-bb9a-ec5fff5b9b4a/ebs_1_480p/index.m3u8'))

@app.route('/eritrea_tv')
def eritrea_tv():
    return(HTML_TEMPLATE.substitute(place_holder='ERITREA TV', place_name='player.mayya.et/play/d0019c9d-5088-47a2-bb9a-ec5fff5b9b4a/eri_1_480p/index.m3u8'))

@app.route('/esat_tv')
def esat_tv():
    return(HTML_TEMPLATE.substitute(place_holder='ESAT TV', place_name='player.mayya.et/play/d0019c9d-5088-47a2-bb9a-ec5fff5b9b4a/esat_1_480p/index.m3u8'))

@app.route('/etv_mezinagna')
def etv_mezinagna():
    return(HTML_TEMPLATE.substitute(place_holder='ETV MEZINAGNA', place_name='player.mayya.et/play/d0019c9d-5088-47a2-bb9a-ec5fff5b9b4a/etv-ent_1_480p/index.m3u8'))

@app.route('/etv_zena')
def etv_zena():
    return(HTML_TEMPLATE.substitute(place_holder='ETV ZENA', place_name='player.mayya.et/play/d0019c9d-5088-47a2-bb9a-ec5fff5b9b4a/etvn_1_480p/index.m3u8'))

@app.route('/fanabc_tv')
def fanabc_tv():
    return(HTML_TEMPLATE.substitute(place_holder='FANABC TV', place_name='player.mayya.et/play/d0019c9d-5088-47a2-bb9a-ec5fff5b9b4a/Fa4ZSvLCw0UJ_480p/index.m3u8'))

@app.route('/nbc_ethiopia_tv')
def nbc_ethiopia_tv():
    return(HTML_TEMPLATE.substitute(place_holder='NBC ETHIOPIA', place_name='player.mayya.et/play/d0019c9d-5088-47a2-bb9a-ec5fff5b9b4a/nbc_eth-1_480p/index.m3u8'))

@app.route('/obn_tv')
def obn_tv():
    return(HTML_TEMPLATE.substitute(place_holder='OBN TV', place_name='player.mayya.et/play/d0019c9d-5088-47a2-bb9a-ec5fff5b9b4a/obn_1_480p/index.m3u8'))

@app.route('/walta_tv')
def walta_tv():
    return(HTML_TEMPLATE.substitute(place_holder='WALTA TV', place_name='player.mayya.et/play/d0019c9d-5088-47a2-bb9a-ec5fff5b9b4a/walta_1_480p/index.m3u8'))

@app.route('/harari_mass_media')
def harari_mass_media():
    return(HTML_TEMPLATE.substitute(place_holder='HARARI MASS MEDIA', place_name='player.mayya.et/play/b83319a5-ac2b-4fcb-889e-38aaafc50f4f/harai-tv_1_360p/index.m3u8'))

@app.route('/abbay_tv')
def abbay_tv():
    return(HTML_TEMPLATE.substitute(place_holder='ABBAY TV', place_name='player.mayya.et/play/d0019c9d-5088-47a2-bb9a-ec5fff5b9b4a/abbay_1_360p/index.m3u8'))

@app.route('/prime_media')
def prime_media():
    return(HTML_TEMPLATE.substitute(place_holder='PRIME MEDIA TV', place_name='player.mayya.et/play/d0019c9d-5088-47a2-bb9a-ec5fff5b9b4a/prime-media_1_480p/index.m3u8'))

@app.route('/sidama_media_network')
def sidama_media_network():
    return(HTML_TEMPLATE.substitute(place_holder='SIDAMA MEDIA NETWORK', place_name='player.mayya.et/play/d0019c9d-5088-47a2-bb9a-ec5fff5b9b4a/smn-tv_1_480p/index.m3u8'))

@app.route('/south_tv')
def south_tv():
    return(HTML_TEMPLATE.substitute(place_holder='SOUTH TV', place_name='player.mayya.et/play/b83319a5-ac2b-4fcb-889e-38aaafc50f4f/south-tv_1_480p/index.m3u8'))

@app.route('/voa_tv_amharic')
def voa_tv_amharic():
    return(HTML_TEMPLATE.substitute(place_holder='VOA TV AMHARIC', place_name='player.mayya.et/play/d0019c9d-5088-47a2-bb9a-ec5fff5b9b4a/voa_1_720p/index.m3u8'))

@app.route('/wolaita_tv')
def wolaita_tv():
    return(HTML_TEMPLATE.substitute(place_holder='WOLAITA TV', place_name='player.mayya.et/play/d0019c9d-5088-47a2-bb9a-ec5fff5b9b4a/wolaita_1_src/index.m3u8'))

@app.route('/ye_ethiopia_lijoch')
def ye_ethiopia_lijoch():
    return(HTML_TEMPLATE.substitute(place_holder='YE ETHIOPIA LIJOCH TV', place_name='player.mayya.et/play/d0019c9d-5088-47a2-bb9a-ec5fff5b9b4a/ethio-lijoch_1_480p/index.m3u8'))
#------------------------------------------

@app.route('/radio')
def radio():
    return render_template('live_radio.html')

#------------Radiio---------------------------
@app.route('/radio_251')
def radio_251():
    return (HTML_TEMPLATE_2.substitute(place_holder2='251 RADIO', place_name='stream.zenolive.com/apzzddhstbruv.aac'))

@app.route('/afro_fm')
def afro_fm():
    return (HTML_TEMPLATE_2.substitute(place_holder2='AFRO 105.3 FM', place_name='stream.zenolive.com/t5td4ky6hkeuv.aac'))

@app.route('/ahadu_fm')
def ahadu_fm():
    return (HTML_TEMPLATE_2.substitute(place_holder2='AHADU 94.3 FM', place_name='stream.zenolive.com/f0pvcuqrwueuv.aac'))

@app.route('/bisrat_fm')
def bisrat_fm():
    return (HTML_TEMPLATE_2.substitute(place_holder2='BISRAT 101.1 FM', place_name='stream.zenolive.com/a4qvycxa2neuv.aac'))

@app.route('/ebc104_fm')
def ebc104_fm():
    return (HTML_TEMPLATE_2.substitute(place_holder2='EBC 104.7 FM', place_name='stream.zenolive.com/2xguamap7yzuv.aac'))

@app.route('/ethiopikalink_radio')
def ethiopikalink_radio():
    return (HTML_TEMPLATE_2.substitute(place_holder2='EthiopikaLink Radio', place_name='stream.zenolive.com/67x9n638rfeuv.aac'))

@app.route('/ebc97_fm')
def ebc97_fm():
    return (HTML_TEMPLATE_2.substitute(place_holder2='FM 97.1', place_name='stream.zenolive.com/rb6wbrap7yzuv.aac'))

@app.route('/mirt_internet_radio')
def mirt_internet_radio():
    return (HTML_TEMPLATE_2.substitute(place_holder2='Mirt Internet Radio', place_name='stream.zenolive.com/0up2tnguawzuv.aac'))

@app.route('/rahel_zeno_radio')
def rahel_zeno_radio():
    return (HTML_TEMPLATE_2.substitute(place_holder2='Rahel Zeno Radio', place_name='stream.zenolive.com/vt1u6fr1h2zuv.aac'))

@app.route('/sheger_fm')
def sheger_fm():
    return (HTML_TEMPLATE_2.substitute(place_holder2='Sheger 102.1 FM', place_name='stream.zenolive.com/kr5k02vagt5tv.aac'))

@app.route('/fana_fm')
def fana_fm():
    return (HTML_TEMPLATE.substitute(place_holder='Fana 98.1 FM', place_name='player.mayya.et/play/d0019c9d-5088-47a2-bb9a-ec5fff5b9b4a/18tGepI8Am2u_src/index.m3u8'))

@app.route('/fana_national_fm')
def fana_national_fm():
    return (HTML_TEMPLATE.substitute(place_holder='Fana National FM', place_name='player.mayya.et/play/d0019c9d-5088-47a2-bb9a-ec5fff5b9b4a/KgwWSDGnFQcH_src/index.m3u8'))

@app.route('/anchoyemusica')
def anchoyemusica():
    return (HTML_TEMPLATE_2.substitute(place_holder2='Anchoye Musica', place_name='stream-43.zeno.fm/um5wuf4spwzuv?zs=vLtdC9FAQ6alYm33WBz0RQ'))

@app.route('/awash_fm')
def awash_fm():
    return (HTML_TEMPLATE_2.substitute(place_holder2='Awash 90.7 FM', place_name='stream-35.zeno.fm/h9ygrpa2wc9uv?zs=2CVNhwx6RNOsJqITrXEafA&rj-ttl=5&rj-tok=AAABfgofc2QApD7mkc0Y3DzF_A'))

@app.route('/axumite_radio')
def axumite_radio():
    return (HTML_TEMPLATE_2.substitute(place_holder2='Axumite Radio', place_name='stream-47.zeno.fm/b9bn18xa2k8uv?zs=xAj6P396S4O9Iw9VoANS3Q'))

@app.route('/endod_radio')
def endod_radio():
    return (HTML_TEMPLATE_2.substitute(place_holder2='Endod Radio', place_name='stream-57.zeno.fm/xff787tfh5zuv?zs=83JK1IXzQhWsrEN-Z2JnKw'))

@app.route('/ethio_tech_radio')
def ethio_tech_radio():
    return (HTML_TEMPLATE_2.substitute(place_holder2='Ethio Tech Radio', place_name='stream-44.zeno.fm/2b0c5v24cy8uv?zs=UWw6kDikSKCBzSinnJu2-g'))

@app.route('/hatricksport_radio')
def hatricksport_radio():
    return (HTML_TEMPLATE_2.substitute(place_holder2='Hatricksport Radio', place_name='stream-47.zeno.fm/t16mzsnrfzzuv?zs=IjnKmA90RYSPShuN62fodw'))

@app.route('/hena_talk_radio')
def hena_talk_radio():
    return (HTML_TEMPLATE_2.substitute(place_holder2='Hena Talk Radio', place_name='stream-42.zeno.fm/g51r6n3z8p8uv?zs=VP9YMXq8Q5m1SbrnDtQ8lA'))

@app.route('/hilawie_radio')
def hilawie_radio():
    return (HTML_TEMPLATE_2.substitute(place_holder2='Hilawie FM', place_name='stream-41.zeno.fm/0dg06w3sy7zuv?zs=3I1QuGzeTX2JgXFIk2mGgw'))

@app.route('/jano_fm')
def jano_fm():
    return (HTML_TEMPLATE_2.substitute(place_holder2='Jano FM', place_name='stream-54.zeno.fm/1cyn1as4v68uv?zs=6ALEcBPQR5Wq6_T-zr8TDw'))

@app.route('/jon_fm')
def jon_fm():
    return (HTML_TEMPLATE_2.substitute(place_holder2='Jon FM Ethiopia', place_name='stream-40.zeno.fm/cx33cb724hhvv?zs=Cdsme55UT5OlML5SAFuVuA'))

@app.route('/voice_of_ethiopia')
def voice_of_ethiopia():
    return (HTML_TEMPLATE_2.substitute(place_holder2='Voice Of Ethiopia Radio', place_name='stream-55.zeno.fm/hubm64kkr2zuv?zs=PFFmvJmuTheHosv7xH_B8g'))

@app.route('/yengat_wege')
def yengat_wege():
    return (HTML_TEMPLATE_2.substitute(place_holder2='Yengat Wege Radio', place_name='stream-40.zeno.fm/pp0d9hyddxquv?zs=i6SccGe7Tn6vb_KYWSEeXQ'))

@app.route('/yonas_kassahun')
def yonas_kassahun():
    return (HTML_TEMPLATE_2.substitute(place_holder2='Yonas Kassahun Radio', place_name='stream-51.zeno.fm/qu0jg6pfjzntv?zs=9ADeJ8mLT-2lGDfFXIaE6w'))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug = True, host = '0.0.0.0', port = port)
