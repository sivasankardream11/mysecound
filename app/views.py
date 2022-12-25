from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def frist(request):
    return HttpResponse('this is my first project')
def suresh(request):
    return HttpResponse('<h1><marquee>hi suresh have a good day</marquee></h1>')
def sanju(request):
    return HttpResponse('<h1>hello sanju</h1>')
def Regform(request):
    return HttpResponse('''
<html>
<head>
  <title>Registration Details</title>
</head>
<body>
  <div>
  <form>
    <fieldset>
  <table>
  <tr>
    <legend>Registration Details</legend>
    <td><label>University:</label></td>
    <td><input type="text"></td>
  </tr>
  <tr>
    <td><label>institute</label></td>
    <td><input type="text"></td>
  </tr>
  <tr>
    <td><label>Branch:</label></td>
    <td>
    <select>
      <option>...select....</option>
      <option>BSC</option>
      <option>BCOM</option>
      <option>BZC</option>
    </select>
  </td>
  </tr>
  <tr>
    <td><label>Degree:</label></td>
    <td>
    <select>
      <option>...select....</option>
      <option>2020</option>
      <option>2021</option>
      <option>2022</option>
    </select>
    <input type="radio" name="r1">persuing
    <input type="radio" name="r1">Completed
  </td>
  </tr>
  <tr>
    <td>
      <label>Average CPI:</label>
    </td>
      <td>
        <select>        
        <option>  </option>
      </select>
        <label>Upto</label>
      <select>
        <option> </option>
      </select>
      <label>Th Semester</label>
    </td>
  </tr>
  <tr>
    <td><label>Experience:</label></td>
    <td>
      <select>
        <option>  </option>
      </select>
      <label>Years</label>
    </td>
  </tr>
  <tr>
    <td><label>Your website or Blog:</label></td>
    <td><input type="text" placeholder="http//"></td>
  </tr>
  </table>
    </fieldset>
  </form>
</div>
</body>
</html>''')
def Displayindianlegeds(reguest):
    return HttpResponse('''
<html>
<head>
  <title>Indian Cricketers</title>
  <style>
    #a
    {
      background-color:yellow;
      color:orangered;
      padding: 10px;
      border: 10px solid black;
    }
    #b
    {
      background-color: blue;
      color: orangered;
      padding: 10px;
      border: 10px solid black;
    }
    #c
    {
      background-color: blue;
      color: orangered;
      padding: 10px;
      border: 10px solid black;
    }
    #d{
      background-color: blue;
      color: orangered;
      padding: 10px;
      border: 10px solid black;
    }
    #e{
      background-color: blue;
      color: orangered;
      padding: 10px;
      border: 10px solid black;
    }
    
  </style>
</head>
<body style="background:linear-gradient;">
<table cellspacing="20px">
  <tr>
    <td><a href="#a">Home</a></td>
    <td><a href="#b">Rohit</a></td>
    <td><a href="#c">KL Rahul</a></td>
    <td><a href="#d">V Kohli</a></td>
    <td><a href="#e">S.Mandhana</a></td>
  </tr>
</table>
    <div id="a">
      <h1>Indian Cricketers</h1>
     </div> 
      <p>The India men's national cricket team, also known as Team India or the Men in Blue,[10] represents India in men's international cricket. It is governed by the Board of Control for Cricket in India (BCCI), and is a Full Member of the International Cricket Council (ICC) with Test, One Day International (ODI) and Twenty20 International (T20I) status.

Cricket was introduced to India by British sailors in the 18th century, and the first cricket club was established in 1792. India's national cricket team played its first international match on 25 June 1932 in a Lord's Test, becoming the sixth team to be granted Test cricket status. India had to wait until 1952, almost twenty years, for its first Test victory. In its first fifty years of international cricket, success was limited, with only 35 wins in 196 Tests. The team, however, gained strength in the 1970s with the emergence of players like Sunil Gavaskar, Gundappa Viswanath, Kapil Dev, and the Indian spin quartet.</p>
<table cellspacing="20px">
  <tr>
    <td><img src="https://wallpapercave.com/wp/wp6848389.jpg" height="370px" width="250px"></td>
    <td><img src="https://wallpapercave.com/wp/wp6848389.jpg" height="370px" width="250px"></td>
  </tr>
</table>
     <p>India's national cricket team played its first international match on 25 June 1932 in a Lord's Test, becoming the sixth team to be granted Test cricket status. India had to wait until 1952, almost twenty years, for its first Test victory. In its first fifty years of international cricket, success was limited, with only 35 wins in 196 Tests. The team, however, gained strength in the 1970s with the emergence of players like Sunil Gavaskar, Gundappa Viswanath, Kapil Dev, and the Indian spin quartet.</p>
 <div id="b">
     <h1>R SHARMA</h1>
 </div>
 <p>Rohit Gurunath Sharma (born 30 April 1987) is an Indian international cricketer who is the current captain of the Indian cricket team in all formats. He is a right-handed opening batsman and considered one of the best white-ball openers to ever play the game. Sharma holds record for scoring most hundreds (5) in a single ICC cricket World Cup. He is going to captain India for the first time in a World Cup in the ongoing T20 World Cup 2022. Sharma captains Mumbai Indians in the Indian Premier League (IPL) and plays for Mumbai in domestic cricket. In the IPL, the Mumbai Indians have won the tournament a record five times under his leadership.

Sharma currently holds the world record for the highest individual score (264) in a one-day international match and is the only player to have scored three double-centuries in one-day internationals. He won the ICC Men's ODI Cricketer of the Year award in 2019 after he scored five centuries in the 2019 World Cup. Sharma has received two national honours, the Arjuna Award in 2015 and the prestigious Major Dhyan Chand Khel Ratna in 2020.</p>
<table cellspacing="20px">
  <tr>
    <td><img src="https://th.bing.com/th/id/OIP.fXOIzgQ5m7X5HpoM_eMkqQHaIy?pid=ImgDet&rs=1" height="340px" width="250px"></td>
    <td><img src="https://i.pinimg.com/736x/42/21/4c/42214cdd963e66e28bc644473de5f2ee.jpg" height="340px" width="250px"></td>
    <td><img src="https://th.bing.com/th/id/OIP.A0nCpYWJWQDjHJxcPHAQhwHaHa?pid=ImgDet&rs=1" height="340px" width="250px"></td>
    <td><img src="https://th.bing.com/th/id/OIP.fXOIzgQ5m7X5HpoM_eMkqQHaIy?pid=ImgDet&rs=1" height="340px" width="250px"></td>
  </tr>
</table>
  <p>In November 2013, during Sachin Tendulkar's farewell series, Sharma made his Test debut at Eden Gardens in Kolkata against West Indies and scored 177, the second-highest score on debut by an Indian to Shikhar Dhawan (187).[15] He followed it up with 111 (not out) in the second Test at his home ground, the Wankhede Stadium in Mumbai.[16]

Having been out of the Test team since 2017–18, Sharma went on the 2018–19 tour of Australia after he had earned a recall earlier. Chief selector M. S. K. Prasad said the reason for his recall was that his natural game suited the bouncy Australian pitches.[17] Sharma played in the first Test in Adelaide, scoring 37 and 1 in an Indian victory.[18][19] During the first Test, he sustained a minor injury which saw him miss the second Test in Perth.[20] He recovered for the Boxing Day third Test at Melbourne and scored 63 (not out) to help India total 443/7 and win both the Test and the series.[21] After the third Test, Sharma had to return to India for the birth of his daughter.[22]

In October 2019, in the third Test against South Africa, Sharma scored his 2,000th run and his first double century in Tests. He made 212 in the first innings of the match.[23][24] Sharma was named as vice-captain of India's Test team during the tour of Australia in 2020, replacing Cheteshwar Pujara.[25][26][27]</p>
    <div id="c">
      <h1>KL RAHUL</h1>
    </div>
    <p>Kannaur Lokesh Rahul (born 18 April 1992) is an Indian international cricketer who currently is the vice-captain of the Indian cricket team in all formats. He is a Right-handed batsman and known for his stylish batting. He plays for Karnataka in domestic cricket and captains Lucknow Super Giants in the Indian Premier League. In the second test against South Africa in January 2022, Rahul captained India for the first time in test cricket and became the 34th Test captain of India.
  Rahul made his international debut in 2014 and scored his maiden Test century in his second Test match. He was the first Indian to score a century on men's One Day International debut,[4] and the third Indian cricketer to score a century in all three formats of international cricket.</p>
<table cellspacing="20px">
  <tr>
    <td><img src="https://indianhotdeal.com/wp-content/uploads/2020/04/KL-rahul.jpeg" height="350px" width="250px"></td>
    <td><img src="https://img.redbull.com/images/c_crop,x_0,y_21,h_1067,w_1600/c_fill,w_1500,h_1000/q_auto,f_auto/redbullcom/2019/03/20/f1485a9f-7c06-45e4-a92d-db37c4479515/kl-rahul-red-bull-athlete-india-cricket-batsman" height="350px" width="250px"></td>
    <td><img src="https://th.bing.com/th/id/R.d4736eba390e040f026e2895351525f5?rik=kD%2fqDRY1siTOZg&riu=http%3a%2f%2fwww.behindwoods.com%2ftamil-movies%2fslideshow%2fforbes-top-100-celeb-earners-where-do-cricketing-stars-stand%2fimages%2fkl-rahul-404-crores-89th-place.jpg&ehk=unaw1uB5fmxLDrPMA84GoTJB6cjTH72h6WxpFLkPqbU%3d&risl=&pid=ImgRaw&r=0" height="350px" width="250px"></td>
    <td><img src="https://i.pinimg.com/originals/04/c6/7b/04c67b340c73ca65f74b0405f3633324.jpg" height="350px" width="250px"></td>
  </tr>
</table>
<p>Rahul made his first-class cricket debut for Karnataka in the 2010–11 season. In the same season he represented his country at the 2010 ICC Under-19 Cricket World Cup, scoring a total of 143 runs in the competition.[14] He made his debut in the Indian Premier League in 2013, for Royal Challengers Bangalore.[15] During the 2013–14 domestic season he scored 1,033 first-class runs, the second highest scorer that season.[citation needed]

Playing for South Zone in the final of the 2014–15 Duleep Trophy against Central Zone, Rahul scored 185 off 233 balls in the first innings and 130 off 152 in the second. He was named the player of the match and selection to the Indian Test squad for the Australian tour followed.

Returning home after the Test series, Rahul became Karnataka's first triple-centurion, scoring 337 against Uttar Pradesh. He went on to score 188 in the 2014–15 Ranji Trophy final against Tamil Nadu and finished the season with an average of 93.11 in the nine matches he played.

</p>
<div id="d">
  <h1> Virat Kohli</h1>
</div>
<p>Virat Kohli (Hindi: [ʋɪˈɾɑːʈ ˈkoːɦliː] (listen); born 5 November[3] 1988) is an Indian international cricketer and former captain of the India national cricket team. He plays for Delhi in domestic cricket and Royal Challengers Bangalore in the Indian Premier League as a right-handed batsman.

Kohli made his Test debut in 2011.[4] He reached the number one spot in the ICC rankings for ODI batsmen for the first time in 2013.[5]  He has won Man of the Tournament twice at the ICC World Twenty20 (in 2014 and 2016). He also holds the world record of being the fastest to score 23,000 international career runs.[6]
Kohli has been the recipient of many awards– most notably the Sir Garfield Sobers Trophy (ICC Men's Cricketer of the Decade): 2011–2020; Sir Garfield Sobers Trophy (ICC Cricketer of the Year) in 2017 and 2018; ICC Test Player of the Year (2018); ICC ODI Player of the Year (2012, 2017, 2018) and Wisden Leading Cricketer in the World (2016, 2017 and 2018).[7] At the national level, he was awarded the Arjuna Award in 2013, the Padma Shri under the sports category in 2017[8] and the Rajiv Gandhi Khel Ratna award, the highest sporting honour in India, in 2018.[9]</p>
<table cellspacing="20px">
  <tr>
    <td><img src="https://th.bing.com/th/id/OIP.JXD7yx26fIiQsbSofwtltgHaJP?pid=ImgDet&rs=1" height="350px" width="250px"></td>
    <td><img src="https://th.bing.com/th/id/OIP.W67-O-tcYNd_7Ee8uS-weAHaJK?pid=ImgDet&rs=1" height="350px" width="250px"></td>
    <td><img src="https://th.bing.com/th/id/OIP.ujR1ZG9UVn6Dfh9EzBYS1AAAAA?pid=ImgDet&rs=1" height="350px" width="250px"></td>
    <td><img src="https://i1.wp.com/timesofindia.indiatimes.com/photo/66218024.cms?resize=816%2C9999&ssl=1" height="350px" width="250px"></td>
  </tr>
</table>
<p>Reacting to the post, famous hair stylist Aalim Hakim commented, 'fab'. "He is looking so hot," a fan commented.

Kohli is currently in the second spot for most runs scored in T20 internationals overall by batters with 3712 runs in 109 games. Despite making his debut only in 2010, Kohli has been far more consistent than most batters in the world, and he has slowly crept up to the second position now. 

Only the current Indian skipper, Rohit Sharma is above him in the race with 3737 runs in 142 matches. With the difference of just 25 runs between the two batters, Kohli will have the chance to move to the top of the list in the upcoming T20 World Cup 2022.

The ICC T20 World Cup 2022 in Australia will start from October 16 and India will play their first match against Pakistan at the Melbourne Cricket Ground (MCG) on October 23.

</p>
<div id="e">
  <h1>S.Mandhana</h1>
</div>
<p>Her first breakthrough came in October 2013, when she became the first Indian woman to achieve a double-hundred in a one-day game. Playing for Maharashtra against Gujarat, she scored an unbeaten 224 off 150 balls in the West Zone Under-19 Tournament, at the Alembic Cricket Ground in Vadodara.[14]

In the 2016 Women's Challenger Trophy, Mandhana scored three half-centuries for India Red in as many games, and helped her team win the trophy by making an unbeaten 62 off 82 balls in the final against India Blue. With 192 runs, she emerged as the tournament's top-scorer.[15]

In September 2016, Mandhana was signed up for a one-year deal with Brisbane Heat for the Women's Big Bash League (WBBL), and along with Harmanpreet Kaur, became one of the first two Indians to be signed up for the League.[16] Playing against Melbourne Renegades in January 2017, she fell awkwardly while fielding after bowling the final ball of her over hurting her knee. She was ruled out of the rest of the tournament which she ended having scored 89 runs in 12 innings.[17][18]

In June 2018, Mandhana signed for Kia Super League defending champions Western Storm, becoming the first Indian to play in the league.[19] In November 2018, she was named in the Hobart Hurricanes' squad for the 2018–19 Women's Big Bash League season.[20][21] In 2021, she was drafted by Southern Brave for the inaugural season of The Hundred.[22] She played for them in 7 games and scored 167 runs before leaving them for India's tour of Australia.[23]
</p>
<table>
  <tr>
    <td><img src="https://th.bing.com/th/id/OIP.1mJTLihxvKS-Um5Ev77olgHaE0?pid=ImgDet&rs=1" height="300px" width="200px"></td>
    <td><img src="https://th.bing.com/th/id/OIP.-xOQpRSCWpWIlRy-Pl8-bAHaE7?pid=ImgDet&w=613&h=408&rs=1" height="300px" width="300px"></td>
    <td><img src="https://images.newindianexpress.com/uploads/user/imagelibrary/2019/9/28/original/Smriti_Mandhana1.jpg" height="300px" width="200px"></td>
    <td><img src="https://gumlet.assettype.com/freepressjournal%2Fimport%2F2018%2F07%2F36898859_489848734797630_6801787493034229760_n.jpg?w=1200&auto=format%2Ccompress&ogImage=true" height="300px" width="200px"></td>
  </tr>
</table>
<p>Mandhana made her Test debut in August 2014 against England at Wormsley Park. She helped her team to win the match by scoring 22 and 51 in her first and second innings, respectively; in the latter innings, she shared in an opening-wicket partnership of 76 runs with Thirush Kamini, chasing 182.[28][29]

In the second ODI game of India's tour of Australia in 2016 at the Bellerive Oval in Hobart, Mandhana scored her maiden international hundred (102 off 109 balls), in a losing cause.[30] Mandhana was the only Indian player to be named in the ICC Women's Team of the Year 2016.[31]

Mandhana came into the team for the 2017 World Cup after recovering from an injury she sustained, an anterior cruciate ligament rupture, during her time at the WBBL in January that year. In her five-month recovery period, she missed the World Cup Qualifier and the Quadrangular Series in South Africa.[32] She began the World Cup with a 90 against England in Derby, in the first of the group matches. She helped her team win by 35 runs, and was named the player of the match.[33] followed by her second hundred in a One Day International against West Indies,(106*)


</p>
</body>
</html>''')