import { useEffect, useState } from 'react';
import './App.css';
import { useForm, SubmitHandler } from "react-hook-form"

type Inputs = {
  url: string
}

function App() {

  const [shortUrl, setShortUrl] = useState<string>()
  const [error, setError] = useState<string>()
  const [urlType, setUrlType] = useState<'short'| 'original'>('short')
  const [history, setHistory] = useState<{id: string, urls: {shortened:string, original:string}[]} | null >(null)

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<Inputs>()
  const onSubmit: SubmitHandler<Inputs> = async  (data) => {
    try {
      const response = await fetch(`http://localhost:8000/${urlType}Url`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
        },
        credentials: "include",
        body: JSON.stringify(data),
      });

      if (!response.ok) {
        const errorData = await response.json();
        setError(errorData.detail);
      } else {
        const responseData = await response.json();
        setShortUrl(responseData.url);
        setError(""); 
      }
    } catch (error) {
      console.error('Error:', error);
      setError('An unexpected error occurred.');
    }
  }

  useEffect(() => {
    fetch('http://localhost:8000/', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
      },
      credentials: "include",
    })
      .then(res => res.json())
      .then(data => {
        console.log(data)
        setHistory(data)
      })
      .catch(err => console.error('Error:', err))
      console.log(history)
  }, [shortUrl])
  

  return (
    <div className="App">
      <h1>Welcome to the UrlShortener</h1>
      <h2>Choose type url</h2>
      <div className='tabs'>
        <button onClick={() => setUrlType('short')} style={urlType === 'short' ? {backgroundColor: 'grey', color: 'white'} : {}}>get shorten URL</button>
        <button onClick={() => setUrlType('original')} style={urlType === 'original' ? {backgroundColor: 'grey', color: 'white'} : {}}>Get original URL</button>
      </div>
      <h3>Enter your URL below:</h3>
      <form onSubmit={handleSubmit(onSubmit)}>
        <div className='group-input'>
          <input {...register("url", { required: true })} />
          {errors.url && <span>This field is required</span>}
          {error && <span style={{color: 'red'}}>{error}</span>}
          <input type="submit" />
        </div>
        {shortUrl &&       
        <p>
          Shortened URL:{' '}
          <a
            href={shortUrl}
            target="_blank"
            rel="noopener noreferrer"
            aria-label={`Shortened URL pointing to ${shortUrl}`}
          >
            {shortUrl}
          </a>
        </p>}
      </form>
      <div>
        <h3>History</h3>
        <div className='group-title'>
          <p>Shortened</p>
          <p>Original</p>
        </div>
        { history && history.urls && history.urls.map((url, index) => (
          <div className='group-input'>
            <a href={url.shortened}
              target="_blank"
              rel="noopener noreferrer"
            >
              {url.shortened}
            </a>
            <a href={url.original}
              target="_blank"
              rel="noopener noreferrer"
            >
              {url.original}
            </a>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
