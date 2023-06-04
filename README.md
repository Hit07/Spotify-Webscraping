# Musical Time Machine Project

# Introduction
The Musical Time Machine project aims to create a Python program that allows users to relive specific moments in their lives through music. By scraping Billboard's Top 100 songs from a chosen date and using the Spotify API, the program generates a playlist with the songs that were popular during that time period. This playlist can serve as a nostalgic gift, enabling users to revisit significant events such as anniversaries, birthdays, or memorable experiences.

# Project Overview
The project involves the following steps:
Scraping the Top 100 Songs: Using the Beautiful Soup library, the program scrapes Billboard's website for the top songs from a specific date within the past 20 years. The song titles and artists are extracted from the list.

Creating a Spotify Playlist: The program utilizes the Spotify API to create a new playlist for the selected date. The playlist will contain the top 100 songs from that particular time period.

Adding Songs to the Playlist: For each song in the scraped list, the program searches for its corresponding track on Spotify. It then adds these tracks to the newly created playlist, ensuring that the playlist accurately reflects the popular music of the chosen date.

Gift and Reminisce: The generated playlist can be shared as a thoughtful gift to evoke memories and transport the recipient back to a specific time in their life. Whether it's for a relationship, a special occasion, or a significant milestone, the playlist serves as a nostalgic reminder of the past.

# How to Use
To utilize the Musical Time Machine, follow these steps:

Clone the project files from the provided GitHub repository.

Install the required dependencies, including Beautiful Soup and the Spotify API client.

Specify the desired date (within the past 20 years) to create a playlist for.

Run the program, which will scrape the Billboard website for the top 100 songs from the chosen date and create a new Spotify playlist.

Share the generated playlist with friends, loved ones, or yourself to relive cherished moments and immerse yourself in the music of the past.

# Conclusion
The Musical Time Machine project combines web scraping techniques with the Spotify API to create personalized playlists based on Billboard's top songs from a chosen date. By enabling users to revisit specific periods in their lives through music, the project offers a unique and sentimental way to reminisce and celebrate meaningful events. Whether it's for a gift or personal enjoyment, the Musical Time Machine adds a touch of nostalgia and transports users back in time, one song at a time.






