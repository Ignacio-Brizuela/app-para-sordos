
        # --- BOTONES ---
        botones_layout = BoxLayout(
            orientation='horizontal', 
            spacing=30, 
            size_hint=(1, 0.5)
        )
        
        btn_texto = BotonGrande(
            texto='Escribir',
            nombre_imagen='habla.png',
            color_bg=COLOR_BTN_TEXTO,
            action=self.on_text_input
        )
        
        btn_mic = BotonGrande(
            texto='Micrófono',
            nombre_imagen='microfono.png', 
            color_bg=COLOR_BTN_MIC,
            action=self.on_mic_input
        )
        
        botones_layout.add_widget(btn_texto)
        botones_layout.add_widget(btn_mic)
        