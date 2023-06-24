import { useEffect, useState } from 'react';
import './App.css';
import MainPage from './pages/MainPage';
import { api } from './js/api';

function App() {
  const [videoId, setVideoId] = useState('');
  const [videoData, setVideoData] = useState('');

  useEffect(() => { // потом нужно будет удалить
    const videoData = {
      fullLength: '00:15:12',
      1: {
        start: '00:00:00',
        end: '00:05:06',
        text: 'Первое предложение',
        screenshots: [
          {
            timecode: '00:01:00',
            link: 'https://unsplash.com/photos/a-man-riding-a-skateboard-up-the-side-of-a-ramp-KH66VBMHnh4',
          },
          {
            timecode: '00:02:00',
            link: 'https://unsplash.com/photos/a-man-standing-on-top-of-a-jeep-in-front-of-a-mountain-T4fCKam9MaU',
          },
          {
            timecode: '00:03:00',
            link: 'https://unsplash.com/photos/a-brown-horse-standing-on-top-of-a-dry-grass-field-zUA7PdtPB-4',
          },
        ],
      },
      2: {
        start: '00:05:07',
        end: '00:10:06',
        text: 'Второе предложение',
        screenshots: [
          {
            timecode: '00:06:00',
            link: 'https://unsplash.com/photos/a-white-and-red-lighthouse-sitting-on-top-of-a-sandy-beach-5jxD7i5CpXc',
          },
          {
            timecode: '00:07:00',
            link: 'https://unsplash.com/photos/a-road-with-a-mountain-in-the-background-JMx8g_JkS2c',
          },
          {
            timecode: '00:08:00',
            link: 'https://unsplash.com/photos/a-person-holding-a-book-in-their-hands-Mg7ZXlpn8rg',
          },
        ],
      },
      3: {
        start: '00:10:07',
        end: '00:15:12',
        text: 'Третье предложение',
        screenshots: [
          {
            timecode: '00:06:00',
            link: 'https://unsplash.com/photos/a-group-of-people-walking-across-a-street-_MnsrCGQcs0',
          },
          {
            timecode: '00:07:00',
            link: 'https://unsplash.com/photos/Cy5dya5MAlI',
          },
          {
            timecode: '00:08:00',
            link: 'https://unsplash.com/photos/a-black-and-white-photo-of-a-human-body-B9zB3LM3_Lo',
          },
        ],
      },
    };
    setVideoData(videoData);
  }, []);

  const getVideoId = (link) => {
    const regex = /[?&]v=([^&]+)/;
    const match = link.match(regex);
    const videoId = match && match[1];
    setVideoId(videoId);
  };

  const fetchAcrticle = (settings) => {
    api
      .postData(settings)
      .then((res) => console.log(res))
      .catch((err) => console.log(err));
  };

  const uploadVideo = (link) => {
    api
      .postData(link)
      .then((res) => console.log(res)) // вот здесь будут сетится данные о видео через setVideoData
      .catch((err) => console.log(err));
  };

  return (
    <div className='App'>
      <MainPage
        uploadVideo={uploadVideo}
        videoData={videoData}
        getVideoId={getVideoId}
        videoId={videoId}
        fetchAcrticle={fetchAcrticle}
      />
    </div>
  );
}

export default App;
