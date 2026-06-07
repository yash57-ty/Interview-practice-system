import React, { useEffect, useState } from 'react'
import { useLocation } from 'react-router-dom'
import api from '../api/axios'
import Navbar from '../components/Navbar'

function Chat() {
    const [message,setmessage]=useState("")
    const [response,setresponse]=useState("")
    const location = useLocation()

    async function sendToChat(msg){
        const token=localStorage.getItem("token")
        try{
            const res=await api.post("/chat",
                {
                    message:msg
                },{
                    headers:{
                        Authorization:`Bearer ${token}`
                    }
                }
            )
            setresponse(res.data.response)
        }
        catch(err){
            console.error(err)
        }
    }

    const sendmessage=async ()=>{
        await sendToChat(message)
    }

    useEffect(()=>{
        const topicName = location.state?.topicName
        if(!topicName) return

        const startMessage = `I want to learn about "${topicName}". Please teach me this topic for interview preparation with explanation, real-world examples, and common interview questions.`
        setmessage(startMessage)
        sendToChat(startMessage)
    },[])
  return (
    <div className="page">
      <Navbar />
      <div className="page-header">
        <h1>AI Interview Assistant</h1>
        <p>
          {location.state?.topicName
            ? `Learning: ${location.state.topicName}`
            : "Ask anything about interview preparation — concepts, examples, and practice questions"}
        </p>
      </div>

      <div className="chat-layout">
        <div className="chat-input-row">
          <input className="input" type="text"
          value={message}
          onChange={(e)=>{setmessage(e.target.value)}}
          placeholder='Ask a question...'
          ></input>
          <button className="btn btn-primary" onClick={sendmessage}>Send</button>
        </div>

        {response && (
          <div className="chat-response-card">
            <h2>AI Response</h2>
            <p>{response}</p>
          </div>
        )}
      </div>
    </div>
  )
}
export default Chat
