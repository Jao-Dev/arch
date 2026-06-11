local keymap = vim.keymap.set
local opts = { noremap = true, silent = true }

keymap("n", "<C-n>", "<cmd>Neotree toggle<CR>", opts)
