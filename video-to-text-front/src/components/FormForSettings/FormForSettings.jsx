import React, { useState } from 'react';
import './FormForSettings.css';
import { InputTime } from '../InputTime/InputTime';
import { FormButton } from '../FormButton/FormButton';
import { useFormWithValidation } from '../../hooks/useFormValidation';

export function FormForSettings({ fetchAcrticle, videoData }) {
  const [values, errors, isValid, handleChange] = useFormWithValidation();
  const [fromStart, setFromStart] = useState(false);
  const [tillEnd, setTillEnd] = useState(false);

  const handleSubmit = (event) => {
    const settings = {
      timeStart: fromStart ? '00:00:00' : values.timeStart,
      timeEnd: tillEnd ? videoData.fullLength : values.timeEnd,
      annotationLength: values.annotationLength,
      articleLength: values.articleLength,
      secondsForScreenshot: values.secondsForScreenshot,
    };
    event.preventDefault();
    fetchAcrticle(settings);
  };

  return (
    <form onSubmit={handleSubmit}>
      <fieldset>
        <ul>
          <li>
            <p>Временной диапазон</p>
            <label htmlFor='video-link'>Начало</label>
            <InputTime
              id='video-link'
              name='timeStart'
              value={
                fromStart
                  ? '00:00:00'
                  : values.timeStart
                  ? values.timeStart
                  : ''
              }
              onChange={handleChange}
              disabled={fromStart ? true : false}
            />
            <span>{errors.timeStart}</span>
            <label htmlFor='from-start'>с начала</label>
            <input
              id='from-start'
              type='checkbox'
              value={fromStart}
              onChange={() => setFromStart(!fromStart)}
            ></input>
            <label htmlFor='video-end'>Конец</label>
            <InputTime
              id='video-end'
              name='timeEnd'
              value={
                tillEnd
                  ? videoData.fullLength
                  : values.timeEnd
                  ? values.timeEnd
                  : ''
              }
              onChange={handleChange}
              disabled={tillEnd ? true : false}
            />
            <span>{errors.timeEnd}</span>
            <label htmlFor='from-end'>до конца</label>
            <input
              id='from-end'
              type='checkbox'
              value={tillEnd}
              onChange={() => setTillEnd(!tillEnd)}
            ></input>
          </li>
          <li>
            <label htmlFor='annotation'>Длина аннотации</label>
            <input
              id='annotation'
              type='number'
              name='annotationLength'
              value={values.annotationLength ? values.annotationLength : ''}
              onChange={handleChange}
            ></input>{' '}
            <span>{errors.annotationLength}</span>
            <label>символов</label>
            <label htmlFor='annotation-unlim'>без ограничения</label>
            <input id='annotation-unlim' type='checkbox'></input>
          </li>
          <li>
            <label htmlFor='article'>Длина статьи</label>
            <input
              id='article'
              type='number'
              name='articleLength'
              value={values.articleLength ? values.articleLength : ''}
              onChange={handleChange}
            ></input>{' '}
            <span>{errors.articleLength}</span>
            <label>символов</label>
            <label htmlFor='article-unlim'>без ограничения</label>
            <input id='article-unlim' type='checkbox'></input>
          </li>
          <li>
            <p>Настройка скриншотов</p>
            <label htmlFor='screenshot'>
              Делать скриншот, если кадр не менялся
            </label>
            <input
              id='screenshot'
              type='number'
              name='secondsForScreenshot'
              value={
                values.secondsForScreenshot ? values.secondsForScreenshot : ''
              }
              onChange={handleChange}
            ></input>{' '}
            <span>{errors.secondsForScreenshot}</span>
            <label>секунд</label>
          </li>
        </ul>
      </fieldset>
      <FormButton disabled={!isValid ? true : false}>Сделать статью</FormButton>
    </form>
  );
}
