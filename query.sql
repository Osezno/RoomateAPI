INSERT INTO public.post_post( title, content , "created", "modified") VALUES ('First post', 'Loremp ipsum dolor amet' , now(), now() ) RETURNING *;