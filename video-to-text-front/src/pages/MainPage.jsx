import React from 'react';
import { FormForSettings } from '../components/FormForSettings/FormForSettings';
import { FormForVideo } from '../components/FormForVideo/FormForVideo';
import Iframe from '../components/Iframe/Iframe';

export default function MainPage({ uploadVideo, getVideoId, videoId, fetchAcrticle }) {
  return (
    <div>
      <h1>Сделать статью из видео</h1>
      <FormForVideo uploadVideo={uploadVideo} getVideoId={getVideoId} />
      <Iframe videoId={videoId} />
      <FormForSettings fetchAcrticle={fetchAcrticle} />
    </div>
  );
}
