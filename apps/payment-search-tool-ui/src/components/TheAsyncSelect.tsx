import React, { useState } from 'react';
import { AsyncPaginate } from 'react-select-async-paginate';

function TheAsyncSelect(props: any) {
  const {
    placeholder,
    textColor,
    emptyOptionMessage,
  } = props

  // set custom style for react select.
  const customStyle = {
    input: (base: any) => ({
      ...base,
      "input:focus": {
        boxShadow: "none",
      },
    }),
    option: (styles: any, state: any) => ({
      ...styles,
      cursor: 'pointer',
    }),
    control: (base: any, state: any) => ({
      ...base,
      fontSize: 14,
      cursor: 'pointer',
      border: state.isFocused && '1px solid #40B4E5 !important',
      boxShadow: state.isFocused && '0 0 0 1px #40B4E5 !important',
    }),
  }


  return (
    <AsyncPaginate
      placeholder={placeholder ?? 'Search'}
      noOptionsMessage={() => emptyOptionMessage || 'No item available'}
      classNamePrefix="dokane"
      theme={(theme: any) => ({
        ...theme,
        colors: {
          ...theme.colors,
          // selected options color
          primary: "blue",
          // placeholder color
          neutral50: `${ textColor  || "black"}`,
        },
      })}
      styles={customStyle}
      debounceTimeout={300}
      {...props}
    />
  );
};

export default TheAsyncSelect