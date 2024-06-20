<a name="readme-top"></a>

<h3 align="center">InspireHealth</h3>

<!-- PROJECT LOGO -->
<br />
<div align="center">
    <img src="InspireHealth.jpg" alt="Logo">
  
  <p align="center">
    InspireHealth provides a structured platform that promotes the needs of hospitals in developing nations and rural areas, with credibility and transparency as our guiding principles.
    <br />
    <a href="https://github.com/your_username/InspireHealth"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="">View Demo</a>
    ·
    <a href="">Report Bug</a>
    ·
    <a href="">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#inspiration">Inspiration</a>
    </li>
    <li>
      <a href="#what-it-does">What it does</a>
    </li>
    <li>
      <a href="#how-we-built-it">How we built it</a>
    </li>
    <li>
      <a href="#challenges-we-ran-into">Challenges we ran into</a>
    </li>
    <li>
      <a href="#accomplishments-that-were-proud-of">Accomplishments that we're proud of</a>
    </li>
    <li>
      <a href="#what-we-learned">What we learned</a>
    </li>
    <li>
      <a href="#whats-next-for-inspirehealth">What's next for InspireHealth</a>
    </li>
    <li>
      <a href="#built-with">Built With</a>
    </li>
  </ol>
</details>

<!-- INSPIRATION -->
## Inspiration

Every time we open social media, we're bombarded by fundraisers -- a GoFundMe, a private donation link, all sorts of crowdfunding platforms -- to the point that it's hard to tell what is credible and where we should focus our money. Those who don't have access to technology, or have limited English proficiency, are often crowded out and shouted over, though their needs are just as worthy and justified. We wanted to create a structured platform that promotes the needs of hospitals in developing nations and rural areas, with credibility and transparency as our guiding principles.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- WHAT IT DOES -->
## What it does

InspireHealth provides a platform for hospitals to create an account, get verified, and run fundraising events and generate direct support. InspireHealth follows fundraisers through the entire process -- hospitals are encouraged to upload videos, photos, and updates to show donors where their money is going and the impact they are having. In order to connect with more global hospitals, InspireHealth uses the Whisper automatic speech recognition system from OpenAI to translate videos and automatically embed highly accurate English subtitles. Finally, InspireHealth has a user-friendly interface with fundraiser spotlights and hospital cards for potential donors to browse and connect with causes close to their hearts.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- HOW WE BUILT IT -->
## How we built it

We used Flask for the back end development and React for the front end to construct a functional and user-friendly website. Additionally, we published our site using a domain name from GoDaddy.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CHALLENGES WE RAN INTO -->
## Challenges we ran into

Our main challenge was creating a unique program that stands apart from more common crowdfunding sites like GoFundMe. In order to fully differentiate our project, we decided to emphasize credibility and transparency, two things we feel are missing from many fundraisers today. We also wanted to create a program that would allow donors to connect strongly with the hospitals they donate to, making donors feel more secure in their donations and encouraging them to continue to give.

On the more technical end, this was everyone's first time using Whisper from OpenAI, leading to many challenges with implementation and ultimately a lot of experimentation and research while building our final working product. This was a very large challenge as we ultimately were able to create a working subtitling program but could not implement into the website. Therefore, it's a next step we would love to work on with more time.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACCOMPLISHMENTS THAT WE'RE PROUD OF -->
## Accomplishments that we're proud of

One accomplishment that we're proud of is implementing Whisper, an automatic speech recognition system, in combination with the moviepy Python library to generate English-translated subtitles for videos in a foreign language. Not only did this take a lot of research and trial and error, but we believe that it will significantly increase the accessibility and reach of InspireHealth. Automatic and highly accurate translations for a wide variety of languages allow fundraisers to connect non-English speakers all over the world to donors, giving a platform and voice to people all over the world whose reach is currently diminished.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- WHAT WE LEARNED -->
## What we learned

We all came in with different levels of experience with programming, and everyone left with expertise in new areas, from constructing website interfaces to working with ASR systems.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- WHAT'S NEXT FOR INSPIREHEALTH -->
## What's next for InspireHealth

With the publishing of the InspireHealth website, we hope to actively begin reaching out to hospitals in rural areas and developing nations, starting with a small number pilot fundraisers and a strong outreach program. After the success of a small launch, we hope to begin reaching more people in need and expanding InspireHealth, including spotlighting current causes and running large-scale campaigns. Hospitals will begin posting campaign results and videos, reach will continue to expand, and ultimately we hope to have a useful, trustworthy, and effective fundraising platform!

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- BUILT WITH -->
## Built With

* [Flask](https://flask.palletsprojects.com/)
* [Python](https://www.python.org/)
* [React](https://reactjs.org/)
* [Whisper](https://github.com/openai/whisper)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
