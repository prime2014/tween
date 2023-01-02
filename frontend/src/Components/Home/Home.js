import React, { useEffect, useState, useCallback } from 'react';
import axios from "axios";


const client = axios.create({
  baseURL: "http://localhost:80",
  headers: {
    "Content-Type": "application/json"
  }
})


const Home = props => {

  const [blogs, setBlogs] = useState([])

  useEffect(()=>{
    client.get("/blog/api/blogs/").then(({ data })=>{
        let { blogs } = data;
        setBlogs(blogs)
    })
  },[])

  return (
    <div>
        <div>
          <h1>Here is a list of blogs I created</h1>

          <div>
            {blogs.map(item=>{
              return (
                <div key={item.id}>
                  <h1>{item.title}</h1>
                  <h5>Written by <i>{item.author}</i></h5>
                  <p>{item.article}</p>
                </div>
              )
            })}
          </div>
        </div>
    </div>
  );
}


export default Home;
