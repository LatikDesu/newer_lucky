import { useState } from 'react';
import './App.css';
import MainPage from './pages/MainPage';
import { api } from './js/api';

function App() {
  const [videoId, setVideoId] = useState('');
  const [videoData, setVideoData] = useState('');

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
        getVideoId={getVideoId}
        videoId={videoId}
        fetchAcrticle={fetchAcrticle}
      />
    </div>
  );
}

export default App;
