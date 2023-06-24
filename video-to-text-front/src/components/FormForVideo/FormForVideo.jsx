import React from 'react';
import './FormForVideo.css';
import { FormButton } from '../FormButton/FormButton';
import { useFormWithValidation } from '../../hooks/useFormValidation';

export function FormForVideo({ uploadVideo, getVideoId }) {
  const [values, errors, isValid, handleChange] = useFormWithValidation();

  const handleSubmit = (event) => {
    event.preventDefault();
    const data = { link: values.link, model: 'base' };
    getVideoId(values.link);
    uploadVideo(data)
  };

  return (
    <form onSubmit={handleSubmit}>
      <fieldset>
        <label htmlFor='video-link'>Полная ссылка на видео</label>
        <input
          id='video-link'
          type='url'
          placeholder='https://www.youtube.com/watch?v=...'
          name='link'
          value={values.link ? values.link : ''}
          onChange={handleChange}
        ></input>
        <span>{errors.link}</span>
      </fieldset>
      <FormButton disabled={!isValid ? true : false}>
        Загрузить видео
      </FormButton>
    </form>
  );
}
