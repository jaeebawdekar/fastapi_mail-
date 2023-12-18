

import { Fragment, useCallback, useContext } from "react"
import { Fragment_054be72e0ea98018059eac5951b3d7a7 } from "/utils/stateful_components"
import { Button, Input, VStack } from "@chakra-ui/react"
import { EventLoopContext, StateContexts } from "/utils/context"
import { Event, set_val } from "/utils/state"
import "focus-visible/dist/focus-visible"
import NextHead from "next/head"



export function Input_9b59c915a3a95278111b750c062fbb15 () {
  const state__email_form_state = useContext(StateContexts.state__email_form_state)


  return (
    <Input name={`message`} placeholder={`Message`} sx={{"multiline": true, "bind": state__email_form_state.message, "padding": "8px", "margin": "8px", "border": "1px solid #ccc", "borderRadius": "4px", "width": "300px"}} type={`text`}/>
  )
}

export function Input_ca288184fdc4bf90472e5613b61c1596 () {
  const state__email_form_state = useContext(StateContexts.state__email_form_state)


  return (
    <Input name={`sender_password`} placeholder={`Sender's Password`} sx={{"bind": state__email_form_state.sender_password, "padding": "8px", "margin": "8px", "border": "1px solid #ccc", "borderRadius": "4px", "width": "300px"}} type={`password`}/>
  )
}

export function Input_4b91da81cba5660619f59d012ddabb7f () {
  const state__email_form_state = useContext(StateContexts.state__email_form_state)


  return (
    <Input name={`sender_email`} placeholder={`Sender's Email`} sx={{"bind": state__email_form_state.sender_email, "padding": "8px", "margin": "8px", "border": "1px solid #ccc", "borderRadius": "4px", "width": "300px"}} type={`email`}/>
  )
}

export function Input_368c55e821d40149f2178c8703043913 () {
  const state__email_form_state = useContext(StateContexts.state__email_form_state)


  return (
    <Input name={`receiver_email`} placeholder={`Receiver's Email`} sx={{"bind": state__email_form_state.receiver_email, "padding": "8px", "margin": "8px", "border": "1px solid #ccc", "borderRadius": "4px", "width": "300px"}} type={`email`}/>
  )
}

export function Button_b1df1091e978d49878e4131aa985b9db () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_click_7fb4de841cc48b91fe987aa332dbcada = useCallback((_e) => addEvents([Event("state.email_form_state.send_email", {})], (_e), {}), [addEvents, Event])

  return (
    <Button onClick={on_click_7fb4de841cc48b91fe987aa332dbcada} sx={{"padding": "10px", "margin": "8px", "background": "#4CAF50", "color": "white", "border": "none", "borderRadius": "4px", "cursor": "pointer"}} type={`submit`}>
  {`Submit`}
</Button>
  )
}

export default function Component() {

  return (
    <Fragment>
  <Fragment_054be72e0ea98018059eac5951b3d7a7/>
  <VStack alignItems={`center`} justifyContent={`center`} spacing={`1em`} sx={{"height": "100vh"}}>
  <Input_4b91da81cba5660619f59d012ddabb7f/>
  <Input_ca288184fdc4bf90472e5613b61c1596/>
  <Input_368c55e821d40149f2178c8703043913/>
  <Input_9b59c915a3a95278111b750c062fbb15/>
  <Button_b1df1091e978d49878e4131aa985b9db/>
</VStack>
  <NextHead>
  <title>
  {`Nextpy App`}
</title>
  <meta content={`A Nextpy app.`} name={`description`}/>
  <meta content={`favicon.ico`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}
