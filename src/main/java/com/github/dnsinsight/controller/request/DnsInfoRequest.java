package com.github.dnsinsight.controller.request;

import lombok.Data;

import javax.validation.constraints.NotBlank;

/**
 * @Author: Tachikoma
 * @Date: 2022-07-02 11:12
 * @Description:
 */
@Data
public class DnsInfoRequest {
    @NotBlank
    private String domain;
    private String dns;
}
