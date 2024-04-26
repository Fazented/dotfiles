import { defineCollection, z } from 'astro:content';
import { format } from 'date-fns';


export const collections = {
	work: defineCollection({
		schema: z.object({
			title: z.string(),
            publishDate: z.string().transform((dateString) => format(new Date(dateString), "yyyy-MM-dd'T'HH:mm:ss")),
			tags: z.array(z.string()),
			img: z.string(),
			img_alt: z.string().optional(),
		}),
	}),
};