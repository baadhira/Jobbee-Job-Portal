import Head from 'next/head'
import Image from 'next/image'
import  Layout  from '../src/components/layout/Layout'
import styles from '../styles/Home.module.css'
import Register from '../src/components/auth/Register'
import axios  from 'axios'
export default function LoginPage() {
  return (
    <Layout title="Login">
      <Register/>
    </Layout>
  )
}