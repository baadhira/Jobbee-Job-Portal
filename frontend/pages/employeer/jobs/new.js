import Head from 'next/head'
import Image from 'next/image'
import  Layout  from '../../../src/components/layout/Layout'
import styles from '../../../styles/Home.module.css'
import NewJob from '../../../src/components/job/NewJob'
import {isAuthenticatedUser} from '../../../utils/isAuthenticated'

export default function NewJobPage({access_token}) {
  return (
    <Layout title="Post a new job">
      <NewJob access_token={access_token} />
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

      return {
          props:{
            access_token,
          }
      }
  }