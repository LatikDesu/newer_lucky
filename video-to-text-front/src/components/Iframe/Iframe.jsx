import React from 'react';
import './Iframe.css';

export default function Iframe({ videoId }) {
  return (
    <div>
      {videoId ? (
        <iframe
          title='iframe'
          allowFullScreen
          src={`https://www.youtube.com/embed/${videoId}`}
        ></iframe>
      ) : (
        <div>Загрузите видео используя полную ссылку</div>
      )}
    </div>
  );
}
