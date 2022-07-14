import Head from 'next/head'
import Image from 'next/image'
import  Layout  from '../../../src/components/layout/Layout'
import styles from '../../../styles/Home.module.css'
import MyJobs from '../../../src/components/job/MyJobs'
import {isAuthenticatedUser} from '../../../utils/isAuthenticated'
import axios from 'axios'

export default function MyJobsPage({jobs,access_token}) {
  return (
    <Layout title="My Jobs">
      <MyJobs access_token={access_token} jobs={jobs} />
    </Layout>
  )
}


export async function getServerSideProps({req}){

  const access_token=req.cookies.access 

  const user=await isAuthenticatedUser(access_token)
  
  if(!user){
    return {
      redirect:{
        destination:"/login",
        permanent:false
      }
    }
  }

  const res=await axios.get(`${process.env.API_URL}/api/me/jobs/`,{
    headers: {
        Authorization: `Bearer ${access_token}`
    }
  })

  const jobs=res.data
      return {
          props:{
            access_token,
            jobs
          }
      }
  }