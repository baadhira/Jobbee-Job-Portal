import Head from 'next/head'
import Image from 'next/image'
import  Layout  from '../src/components/layout/Layout'
import styles from '../styles/Home.module.css'
import Login from '../src/components/auth/Login'
import axios  from 'axios'
export default function LoginPage() {
  return (
    <Layout title="Login">
      <Login/>
    </Layout>
  )
}