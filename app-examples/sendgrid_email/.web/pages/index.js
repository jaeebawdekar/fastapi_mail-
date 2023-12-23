

import { Fragment, useCallback, useContext } from "react"
import { Fragment_054be72e0ea98018059eac5951b3d7a7 } from "/utils/stateful_components"
import { Button, Input, VStack } from "@chakra-ui/react"
import { EventLoopContext, StateContexts } from "/utils/context"
import { Event, set_val } from "/utils/state"
import "focus-visible/dist/focus-visible"
import NextHead from "next/head"



export function Input_4b91da81cba5660619f59d012ddabb7f () {
  const state__email_form_state = useContext(StateContexts.state__email_form_state)


  return (
    <Input name={`sender_email`} placeholder={`Sender's Email`} sx={{"bind": state__email_form_state.sender_email, "padding": "8px", "margin": "8px", "border": "1px solid #ccc", "borderRadius": "4px", "width": "300px"}} type={`email`}/>
  )
}

export function Input_bb84eb8cec9a6d71494a5b57b6d19e19 () {
  const state__email_form_state = useContext(StateContexts.state__email_form_state)


  return (
    <Input name={`api_key`} placeholder={`SendGrid API Key`} sx={{"bind": state__email_form_state.api_key, "padding": "8px", "margin": "8px", "border": "1px solid #ccc", "borderRadius": "4px", "width": "300px"}} type={`password`}/>
  )
}

export function Input_9b59c915a3a95278111b750c062fbb15 () {
  const state__email_form_state = useContext(StateContexts.state__email_form_state)


  return (
    <Input name={`message`} placeholder={`Message`} sx={{"multiline": true, "bind": state__email_form_state.message, "padding": "8px", "margin": "8px", "border": "1px solid #ccc", "borderRadius": "4px", "width": "300px"}} type={`text`}/>
  )
}

export function Button_1a785e04945f0e91a9a56183d7351f0f () {
  const state__email_form_state = useContext(StateContexts.state__email_form_state)
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_click_64f15d9a5d9eeee1791ab4d1df68c505 = useCallback((_e) => addEvents([Event("state.email_form_state.send_email", {sender_email:state__email_form_state.sender_email,api_key:state__email_form_state.api_key,receiver_email:state__email_form_state.receiver_email,message:state__email_form_state.message})], (_e), {}), [addEvents, Event, state__email_form_state, state__email_form_state, state__email_form_state, state__email_form_state])

  return (
    <Button onClick={on_click_64f15d9a5d9eeee1791ab4d1df68c505} sx={{"padding": "10px", "margin": "8px", "background": "#4CAF50", "color": "white", "border": "none", "borderRadius": "4px", "cursor": "pointer"}} type={`submit`}>
  {`Submit`}
</Button>
  )
}

export function Input_368c55e821d40149f2178c8703043913 () {
  const state__email_form_state = useContext(StateContexts.state__email_form_state)


  return (
    <Input name={`receiver_email`} placeholder={`Receiver's Email`} sx={{"bind": state__email_form_state.receiver_email, "padding": "8px", "margin": "8px", "border": "1px solid #ccc", "borderRadius": "4px", "width": "300px"}} type={`email`}/>
  )
}

export default function Component() {

  return (
    <Fragment>
  <Fragment_054be72e0ea98018059eac5951b3d7a7/>
  <VStack alignItems={`center`} justifyContent={`center`} spacing={`1em`} sx={{"height": "100vh"}}>
  <Input_4b91da81cba5660619f59d012ddabb7f/>
  <Input_bb84eb8cec9a6d71494a5b57b6d19e19/>
  <Input_368c55e821d40149f2178c8703043913/>
  <Input_9b59c915a3a95278111b750c062fbb15/>
  <Button_1a785e04945f0e91a9a56183d7351f0f/>
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
