import Head from 'next/head'
import Image from 'next/image'
import  Layout  from '../../src/components/layout/Layout'
import styles from '../../styles/Home.module.css'
import JobsApplied from '../../src/components/job/JobsApplied'
import axios  from 'axios'
import {isAuthenticatedUser} from '../../utils/isAuthenticated'

export default function JobsAppliedPage({jobs}) {
    console.log(jobs,"jobs aplied");
  return (
    <Layout title="Jobs Applied">
      <JobsApplied jobs={jobs} />
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
  const res=await axios.get(`${process.env.API_URL}/api/me/jobs/applied/`,{
    headers:{
        Authorization:`Bearer ${access_token}`
    }
  })

  const jobs=res.data
      return {
          props:{
            jobs,
          }
      }
  }

 